import pandas as pd
import pandas_ta as ta

def calculate_indicators(df):
    """
    Calculates technical indicators using pandas-ta.
    Expects a DataFrame with 'Open', 'High', 'Low', 'Close', 'Volume' columns.
    
    Returns the DataFrame with added indicator columns mapped to the database schema.
    """
    if df.empty:
        return df

    # Create a copy to avoid SettingWithCopy warnings on the original
    df = df.copy()

    try:
        # ADX
        # Returns DataFrame with ADX_14, DMP_14, DMN_14
        adx = df.ta.adx(length=14)
        if adx is not None:
            # Find the ADX column (starts with ADX)
            for col in adx.columns:
                if col.startswith('ADX'):
                    df['adx_14'] = adx[col]
                    break
        
        # RSI
        # Returns Series
        rsi = df.ta.rsi(length=14)
        if rsi is not None:
            df['rsi_14'] = rsi

        # BBANDS
        # Returns DataFrame with Lower, Mid, Upper, Bandwidth, Percent
        bb = df.ta.bbands(length=20, std=2.0)
        if bb is not None:
            for col in bb.columns:
                if col.startswith('BBU'):
                    df['bb_upper'] = bb[col]
                elif col.startswith('BBL'):
                    df['bb_lower'] = bb[col]
                elif col.startswith('BBB'):
                    df['bb_width'] = bb[col]

        # MACD
        # Returns DataFrame with MACD, Histogram, Signal
        macd = df.ta.macd(fast=12, slow=26, signal=9)
        if macd is not None:
            for col in macd.columns:
                # MACD_... is the line
                # MACDs_... is the signal
                # MACDh_... is the histogram
                if col.startswith('MACD_'):
                    df['macd_line'] = macd[col]
                elif col.startswith('MACDs'):
                    df['macd_signal'] = macd[col]

    except Exception as e:
        print(f"Error calculating indicators: {e}")
        return df

    # Ensure all expected columns exist (fill with NaN if calculation failed or insufficient data)
    expected_cols = ['adx_14', 'rsi_14', 'bb_upper', 'bb_lower', 'bb_width', 'macd_line', 'macd_signal']
    for col in expected_cols:
        if col not in df.columns:
            df[col] = None
            
    return df
