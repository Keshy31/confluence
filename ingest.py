import yfinance as yf
import pandas as pd
from config import WATCHLIST, DB_PATH
from modules import database, indicators
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_ticker(ticker, con):
    """
    Fetches data for a single ticker and inserts it into the database.
    """
    logging.info(f"Processing {ticker}...")
    
    # Define timeframes to fetch
    timeframes = [
        {'tf': '1d', 'period': '1y', 'interval': '1d'},
        {'tf': '1h', 'period': '60d', 'interval': '1h'}
    ]
    
    for settings in timeframes:
        try:
            # Fetch data
            # auto_adjust=True accounts for splits/dividends
            df = yf.download(
                ticker, 
                period=settings['period'], 
                interval=settings['interval'], 
                progress=False,
                auto_adjust=True,
                multi_level_index=False 
            )
            
            if df.empty:
                logging.warning(f"No data for {ticker} ({settings['tf']})")
                continue
            
            # Reset index to get timestamp as a column
            df = df.reset_index()
            
            # Clean column names (Datetime/Date -> timestamp)
            if 'Date' in df.columns:
                df = df.rename(columns={'Date': 'timestamp'})
            elif 'Datetime' in df.columns:
                 df = df.rename(columns={'Datetime': 'timestamp'})
            
            # Handle potential capitalization differences or whitespace
            df.columns = [c.strip() for c in df.columns]

            # Timezone handling: Convert to Naive UTC
            if pd.api.types.is_datetime64_any_dtype(df['timestamp']):
                if df['timestamp'].dt.tz is not None:
                     df['timestamp'] = df['timestamp'].dt.tz_convert('UTC').dt.tz_localize(None)
                else:
                    # If naive, assume it's already relevant (or convert if needed). 
                    # Daily data from yfinance is usually naive.
                    pass

            # Lowercase all columns for consistency with modules
            df.columns = [c.lower() for c in df.columns]
            
            # Calculate Indicators
            df = indicators.calculate_indicators(df)
            
            # Prepare for DB
            df['ticker'] = ticker
            df['timeframe'] = settings['tf']
            
            # Select and Order columns to match DB schema
            required_cols = [
                'ticker', 'timeframe', 'timestamp', 
                'open', 'high', 'low', 'close', 'volume',
                'adx_14', 'rsi_14', 
                'bb_upper', 'bb_lower', 'bb_width', 
                'macd_line', 'macd_signal'
            ]
            
            # Ensure only required columns are present
            # Fill missing columns with None/NaN if calculation failed
            for col in required_cols:
                if col not in df.columns:
                    df[col] = None
            
            final_df = df[required_cols]
            
            # Insert into DuckDB
            # We use INSERT OR REPLACE (upsert)
            con.execute("INSERT OR REPLACE INTO candles SELECT * FROM final_df")
            
        except Exception as e:
            logging.error(f"Error processing {ticker} {settings['tf']}: {e}")

def main():
    try:
        logging.info("Starting ingestion...")
        con = database.get_connection(DB_PATH)
        database.initialize_schema(con)
        
        for ticker in WATCHLIST:
            process_ticker(ticker, con)
            
        logging.info("Ingestion complete.")
        
        # Verification Query
        result = con.execute("SELECT ticker, timeframe, count(*) as count FROM candles GROUP BY ticker, timeframe ORDER BY ticker, timeframe").fetchall()
        logging.info("Data Verification (Row Counts):")
        for row in result:
            logging.info(f"  {row}")
            
        # Verify Scanner Matrix View
        matrix = con.execute("SELECT * FROM scanner_matrix LIMIT 5").fetchdf()
        if not matrix.empty:
            logging.info("\nScanner Matrix Preview:")
            logging.info(matrix.to_string())
        else:
            logging.warning("Scanner Matrix is empty.")
            
        con.close()
        
    except Exception as e:
        logging.critical(f"Ingestion failed: {e}")

if __name__ == "__main__":
    main()

