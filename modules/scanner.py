import duckdb
import pandas as pd
import logging
from modules.database import get_connection
from config import DB_PATH

class Scanner:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path

    def get_matrix(self):
        """
        Fetches the scanner matrix from the database and calculates the status.
        Returns a list of dictionaries ready for AgGrid.
        """
        con = get_connection(self.db_path)
        try:
            # Check if view exists first to avoid hard crash if schema not init
            # (Though we expect it to be init)
            df = con.execute("SELECT * FROM scanner_matrix").fetchdf()
            
            if df.empty:
                return []
            
            # Apply protocol logic
            
            # 1. Regime (Daily ADX)
            # ADX > 25 -> Trending, else Ranging
            df['regime'] = df['daily_adx'].apply(lambda x: 'TRENDING' if x is not None and x > 25 else 'RANGING')
            
            # 2. Volatility (Hourly BB Width)
            # Squeeze if width <= min_width_20 * 1.1
            def check_squeeze(row):
                if pd.isna(row['hourly_bb_width']) or pd.isna(row['hourly_min_bb_width_20']):
                    return 'NORMAL'
                if row['hourly_bb_width'] <= row['hourly_min_bb_width_20'] * 1.1:
                    return 'SQUEEZE'
                return 'NORMAL'
            
            df['volatility'] = df.apply(check_squeeze, axis=1)
            
            # 3. Momentum (Hourly RSI)
            # > 70 Overbought, < 30 Oversold, else Neutral
            def check_rsi(val):
                if pd.isna(val): return 'NEUTRAL'
                if val > 70: return 'OVERBOUGHT'
                if val < 30: return 'OVERSOLD'
                return 'NEUTRAL'
            
            df['momentum'] = df['hourly_rsi'].apply(check_rsi)
            
            # 4. Direction (MACD)
            # MACD > Signal -> Bullish, else Bearish
            def check_direction(row):
                if pd.isna(row['hourly_macd_line']) or pd.isna(row['hourly_macd_signal']):
                    return 'NEUTRAL'
                return 'BULLISH' if row['hourly_macd_line'] > row['hourly_macd_signal'] else 'BEARISH'
                
            df['direction'] = df.apply(check_direction, axis=1)
            
            # 5. Composite Status (The "Confluence" Logic)
            def calculate_confluence(row):
                # Basic Statuses
                
                is_trending = row['regime'] == 'TRENDING'
                is_ranging = row['regime'] == 'RANGING'
                is_squeeze = row['volatility'] == 'SQUEEZE'
                is_oversold = row['momentum'] == 'OVERSOLD'
                is_overbought = row['momentum'] == 'OVERBOUGHT'
                is_bullish = row['direction'] == 'BULLISH'
                is_bearish = row['direction'] == 'BEARISH'
                
                # Squeeze Logic - High Priority
                if is_squeeze:
                    return "SQUEEZE"
                
                # Trend Following Pullbacks
                if is_trending:
                    if is_bullish and is_oversold:
                        return "BULLISH PULLBACK"
                    if is_bearish and is_overbought:
                        return "BEARISH PULLBACK"
                    return "TRENDING"

                # Range Trading
                if is_ranging:
                    if is_oversold and is_bullish: # Reversal from bottom
                        return "RANGE BUY"
                    if is_overbought and is_bearish: # Reversal from top
                        return "RANGE SELL"
                    return "RANGING"
                    
                return "WAIT"

            df['status'] = df.apply(calculate_confluence, axis=1)
            
            # Round floats for display
            float_cols = ['daily_adx', 'hourly_rsi', 'hourly_bb_width', 'current_price']
            for col in float_cols:
                if col in df.columns:
                    df[col] = df[col].round(2)
            
            # Convert Timestamps to string for JSON serialization
            if 'last_updated' in df.columns:
                df['last_updated'] = df['last_updated'].astype(str)

            return df.to_dict('records')
            
        except Exception as e:
            logging.error(f"Error calculating scanner matrix: {e}")
            return []
        finally:
            con.close()

