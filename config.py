# Ticker Watchlist
WATCHLIST = [
    "SPY", "QQQ", "IWM",  # Indices
    "AAPL", "NVDA", "MSFT", "TSLA", "AMD", "AMZN", "GOOGL", "META" # Tech
]

# Indicator Settings
INDICATORS = {
    "ADX_LENGTH": 14,
    "RSI_LENGTH": 14,
    "BB_LENGTH": 20,
    "BB_STD": 2.0,
    "MACD_FAST": 12,
    "MACD_SLOW": 26,
    "MACD_SIGNAL": 9
}

# Database
DB_PATH = "market_data.duckdb"

