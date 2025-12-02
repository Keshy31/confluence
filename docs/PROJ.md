# Project Confluence: The Algorithmic Market Scanner

## 1. Executive Summary

**Project Confluence** is a local, web-based dashboard designed for Swing Traders. Unlike traditional portfolio trackers, this is a **Market Scanner**. It monitors a watchlist of assets (e.g., the S&P 500 or specific sectors) to identify high-probability setups in real-time.

It automates the cognitive load of the **Confluence Protocol** by mechanically filtering assets through a "Traffic Light" system, allowing the trader to focus only on assets that meet strict criteria for Regime, Volatility, and Momentum.

## 2. Theoretical Framework

The system automates the decision-making process defined in the protocol:

1.  **Phase 0: The Regime (Daily Data)**
    * *Question:* Are we Trending or Ranging?
    * *Indicator:* **ADX (14)** on Daily timeframe.
    * *Logic:* ADX > 25 = Trend Mode; ADX < 25 = Range Mode.
2.  **Phase 1: The Setup (Hourly Data)**
    * *Question:* Is there a valid setup for the current regime?
    * *Indicators:* **Bollinger Bands** (Volatility Squeeze), **MACD** (Trend Direction), **RSI** (Momentum Health).
3.  **Phase 2: The Trigger (Price Action)**
    * *Question:* Is there a confirmation candle?
    * *Logic:* Automated detection of key patterns (Hammer, Engulfing) on the Hourly timeframe.

## 3. System Architecture

We utilize a **Modern Data Stack** pattern, separating data ingestion from the user interface to ensure high performance (zero UI lag) even when tracking 50+ tickers.

### Tech Stack

* **Language:** Python 3.10+
* **UI Framework:** `NiceGUI` (Modern, event-driven web UI based on Vue.js).
* **Data Grid:** `AgGrid` (Enterprise-grade tables for the scanner view).
* **Charting:** `Plotly` (Interactive financial charts).
* **Data Source:** `OpenBB Platform` (configured with `yfinance` provider).
* **Storage/Analytics:** `DuckDB` (High-performance in-process OLAP database).
* **Technical Analysis:** `pandas-ta` (Vectorized indicator calculation).

### Data Flow Diagram

```mermaid
graph TD
    subgraph "Background Service (Ingest)"
        A[Ticker List] --> B[OpenBB / YFinance]
        B --> |Fetch Daily & Hourly| C[Pandas-TA Processor]
        C --> |Calculate Indicators| D[(DuckDB: market_data.db)]
    end

    subgraph "Frontend (NiceGUI)"
        D --> |SQL Query: Signal Matrix| E[AgGrid Scanner]
        D --> |SQL Query: OHLCV| F[Plotly Chart Deck]
        E --> |Click Row| F
    end
````

## 4\. Data Strategy

### A. The "Hybrid Timeframe" Model

To execute the protocol, we must maintain two distinct time-series for every ticker:

1.  **Daily:** Used strictly for **Regime Detection** (Phase 0).
2.  **Hourly:** Used for **Trigger Execution** (Phase 1 & 2).

### B. Database Schema (DuckDB)

We use DuckDB for its ability to handle "As-Of" joins and extremely fast analytical queries.

**Table: `candles`**

```sql
CREATE TABLE candles (
    ticker VARCHAR,
    timeframe VARCHAR, -- '1d' or '1h'
    timestamp TIMESTAMP,
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume BIGINT,
    -- Pre-calculated Indicators
    adx_14 DOUBLE,
    rsi_14 DOUBLE,
    bb_upper DOUBLE,
    bb_lower DOUBLE,
    bb_width DOUBLE,
    macd_line DOUBLE,
    macd_signal DOUBLE,
    PRIMARY KEY (ticker, timeframe, timestamp)
);
```

### C. Ingestion Logic

A background script (`ingest.py`) runs periodically (e.g., every hour):

1.  Fetches last 60 days of Hourly data + 1 Year of Daily data.
2.  Computes all indicators using `pandas-ta`.
3.  Performs an **Upsert** (Insert or Replace) into DuckDB.

## 5\. Development Phases

### Phase 1: The Data Engine

  * **Goal:** Successfully fetch, process, and store data.
  * **Deliverables:**
      * `config.py`: Ticker list and Indicator settings.
      * `modules/ingest.py`: Script to fetch OpenBB data and save to DuckDB.
      * `modules/database.py`: DuckDB connection and schema management.
  * **Verification:** Query DuckDB to see populated tables with ADX values.

### Phase 2: The Scanner Logic

  * **Goal:** Query the DB to build the "Signal Matrix."
  * **Deliverables:**
      * `modules/scanner.py`: A class that executes a SQL query to get the *latest* state for every ticker.
      * **Logic:**
          * Determine Status: "WAIT", "WATCH", or "READY" based on Protocol rules.
          * Example: IF `Daily_ADX > 25` AND `Hourly_RSI < 30` -\> Status = "PULLBACK READY".

### Phase 3: The Dashboard (UI)

  * **Goal:** Visualize the data with NiceGUI.
  * **Deliverables:**
      * **Left Panel (Scanner):** An AgGrid table displaying Ticker, Price, Regime (Daily), and Setup (Hourly).
      * **Right Panel (Analysis):**
          * Top: Hourly Candlestick Chart (Plotly) with Bollinger Bands.
          * Bottom: Multi-pane indicator stack (RSI, MACD).
      * **Interaction:** Clicking a row in AgGrid instantly updates the charts.

### Phase 4: The "Perfect Trade" Assistant

  * **Goal:** Add specific trade execution helpers.
  * **Deliverables:**
      * **Checklist Widget:** A sidebar that explicitly checks off Protocol rules for the selected ticker.
      * **Risk Calculator:** Input box for "Account Size" that auto-calculates Position Size based on the ATR Stop Loss.

## 6\. Project Directory Structure

```text
project_confluence/
├── .env                  # Environment variables
├── main.py               # Entry point (NiceGUI App)
├── ingest.py             # Background data fetcher script
├── config.py             # Constants & Ticker Watchlist
├── market_data.duckdb    # The Database File
├── modules/
│   ├── __init__.py
│   ├── database.py       # DuckDB wrappers
│   ├── indicators.py     # Pandas-TA logic
│   ├── scanner.py        # SQL queries for the matrix
│   └── ui_components.py  # Chart & Grid definitions
└── requirements.txt      # nicegui, openbb, duckdb, pandas-ta, plotly
```
