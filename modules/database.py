import duckdb
import logging

def get_connection(db_path="market_data.duckdb"):
    """
    Establishes a connection to the DuckDB database.
    """
    try:
        con = duckdb.connect(db_path)
        return con
    except Exception as e:
        logging.error(f"Failed to connect to database: {e}")
        raise

def initialize_schema(con):
    """
    Creates the necessary tables and views if they don't exist.
    """
    try:
        # Create candles table
        con.execute("""
            CREATE TABLE IF NOT EXISTS candles (
                ticker VARCHAR,
                timeframe VARCHAR, -- '1d' or '1h'
                timestamp TIMESTAMP,
                open DOUBLE,
                high DOUBLE,
                low DOUBLE,
                close DOUBLE,
                volume BIGINT,
                
                -- Calculated Indicators
                adx_14 DOUBLE,
                rsi_14 DOUBLE,
                bb_upper DOUBLE,
                bb_lower DOUBLE,
                bb_width DOUBLE,
                macd_line DOUBLE,
                macd_signal DOUBLE,
                
                PRIMARY KEY (ticker, timeframe, timestamp)
            );
        """)
        
        # Create scanner_matrix view
        # We use CREATE OR REPLACE VIEW to ensure it's up to date
        con.execute("""
            CREATE OR REPLACE VIEW scanner_matrix AS
            WITH hourly_data AS (
                SELECT 
                    *,
                    MIN(bb_width) OVER (
                        PARTITION BY ticker 
                        ORDER BY timestamp 
                        ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
                    ) as min_bb_width_20
                FROM candles 
                WHERE timeframe = '1h'
            ),
            latest_hourly AS (
                SELECT * 
                FROM hourly_data 
                QUALIFY ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY timestamp DESC) = 1
            ),
            latest_daily AS (
                SELECT * 
                FROM candles 
                WHERE timeframe = '1d' 
                QUALIFY ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY timestamp DESC) = 1
            )
            SELECT 
                d.ticker,
                d.adx_14 as daily_adx,
                h.rsi_14 as hourly_rsi,
                h.bb_width as hourly_bb_width,
                h.min_bb_width_20 as hourly_min_bb_width_20,
                h.macd_line as hourly_macd_line,
                h.macd_signal as hourly_macd_signal,
                h.close as current_price,
                h.timestamp as last_updated
            FROM latest_daily d
            JOIN latest_hourly h ON d.ticker = h.ticker;
        """)
        
        logging.info("Database schema initialized successfully.")
        
    except Exception as e:
        logging.error(f"Failed to initialize schema: {e}")
        raise

