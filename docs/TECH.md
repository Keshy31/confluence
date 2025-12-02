# Technical Specification: Project Confluence

**Version:** 1.0
**Type:** High-Performance Market Scanner
**Target System:** Local Web Server (Python/NiceGUI)

## 1. System Overview

Project Confluence is a local web application that monitors a watchlist of assets for specific technical setups. Unlike standard chart tools, it uses an **OLAP database (DuckDB)** to query technical indicators across multiple timeframes instantly, presenting a "Ranked" or "Filtered" list of opportunities to the trader.

**Core Philosophy:** "Scanning over Scrolling." The system processes data in the background and only surfaces assets that meet the **Confluence Protocol** criteria.

## 2. Architecture & Tech Stack

We use a **Decoupled Architecture**: The Data Ingestion service runs independently of the User Interface to ensure the dashboard remains responsive (60fps) even during heavy data processing.

### The Stack
* **Frontend:** `NiceGUI` (Vue.js wrapper for Python) - chosen for reactive state management.
* **Grid Component:** `AgGrid` (via NiceGUI) - chosen for Excel-like filtering and sorting.
* **Database:** `DuckDB` - chosen for high-speed analytical queries on time-series data.
* **Data Provider:** `OpenBB Platform` (Provider: `yfinance`).
* **Math Engine:** `pandas-ta` (Vectorized Technical Analysis).

### Data Flow

```mermaid
graph LR
    subgraph "Background Process"
        A[Cron Job] -->|Trigger| B[ingest.py]
        B -->|Fetch OHLCV| C[OpenBB SDK]
        C -->|DataFrames| D[Pandas-TA]
        D -->|Compute Indicators| E[(DuckDB)]
    end

    subgraph "User Interface"
        F[NiceGUI Client] -->|Poll/Event| G[Scanner Query]
        G -->|SQL Select| E
        E -->|Result Set| H[AgGrid Table]
        H -->|Click Row| I[Update Plotly Chart]
    end
````

## 3\. Database Design (DuckDB)

The system relies on a single persistent DuckDB file: `market_data.duckdb`.

### Table: `candles`

This table stores both Daily and Hourly data in a unified schema to facilitate "Hybrid Timeframe" queries.

```sql
CREATE TABLE IF NOT EXISTS candles (
    ticker VARCHAR,          -- e.g., 'AAPL'
    timeframe VARCHAR,       -- '1d' or '1h'
    timestamp TIMESTAMP,     -- UTC
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume BIGINT,
    
    -- Calculated Indicators (Phase 0 & 1)
    adx_14 DOUBLE,           -- Trend Strength
    rsi_14 DOUBLE,           -- Momentum
    bb_upper DOUBLE,         -- Volatility
    bb_lower DOUBLE,
    bb_width DOUBLE,         -- Bandwidth for Squeeze detection
    macd_line DOUBLE,        -- Trend Direction
    macd_signal DOUBLE,
    
    PRIMARY KEY (ticker, timeframe, timestamp)
);
```

### View: `scanner_matrix`

A view to simplify the frontend query. It joins the latest Daily record (for Regime) with the latest Hourly record (for Trigger).

```sql
CREATE VIEW scanner_matrix AS
SELECT 
    d.ticker,
    d.adx_14 as daily_adx,
    h.rsi_14 as hourly_rsi,
    h.bb_width as hourly_bb_width,
    h.close as current_price,
    h.timestamp as last_updated
FROM (SELECT * FROM candles WHERE timeframe = '1d' QUALIFY ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY timestamp DESC) = 1) d
JOIN (SELECT * FROM candles WHERE timeframe = '1h' QUALIFY ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY timestamp DESC) = 1) h
ON d.ticker = h.ticker;
```

## 4\. Ingestion Engine (`ingest.py`)

This script is the heartbeat of the system. It handles the "Confluence" math before storage.

**Requirements:**

1.  **Watchlist:** Load tickers from `config.py`.
2.  **Fetch:**
      * **Daily:** 1 Year history (required for stable ADX calculation).
      * **Hourly:** 60 Days history.
3.  **Process (`pandas-ta`):**
      * `df.ta.adx(length=14)`
      * `df.ta.rsi(length=14)`
      * `df.ta.bbands(length=20, std=2.0)` -\> Calculate `width = (upper - lower) / mid`
      * `df.ta.macd(fast=12, slow=26, signal=9)`
4.  **Storage:** Use `duckdb.sql("INSERT OR REPLACE INTO candles ...")`.

## 5\. Logic Algorithms (The "Protocol")

The frontend must translate raw numbers into "Confluence Statuses".

**1. Regime Filter (Daily Data)**

  * *Input:* `daily_adx`
  * *Logic:*
      * IF `> 25`: Return `TRENDING` (Green)
      * IF `< 25`: Return `RANGING` (Gray)

**2. Volatility State (Hourly Data)**

  * *Input:* `hourly_bb_width`
  * *Logic:* Compare current width to 20-period minimum.
      * IF `width <= min(width, 20) * 1.1`: Return `SQUEEZE` (Yellow) -\> *Setup Ready*

**3. Momentum State (Hourly Data)**

  * *Input:* `hourly_rsi`
  * *Logic:*
      * IF `> 70`: Return `OVERBOUGHT` (Red)
      * IF `< 30`: Return `OVERSOLD` (Green)
      * ELSE: `NEUTRAL`

## 6\. UI/UX Specification

### Layout

  * **Framework:** NiceGUI (`ui.row`, `ui.column`, `ui.splitter`).
  * **Splitter:** 30% Left (Grid), 70% Right (Charts).

### Left Panel: The Signal Matrix (AgGrid)

Columns definition with conditional formatting:

| Header | Field | Rendering Logic |
| :--- | :--- | :--- |
| **Ticker** | `ticker` | Bold text |
| **Regime** | `daily_adx` | Cell Color: Green if \> 25, Gray if \< 25 |
| **RSI (H1)** | `hourly_rsi` | Text Color: Red if \> 70, Green if \< 30 |
| **Vol** | `hourly_bb_width` | Badge: "SQZ" if Squeeze detected |
| **Price** | `current_price` | Standard currency format |

### Right Panel: The Deep Dive (Plotly)

A `plotly.graph_objects` figure with **shared X-axis** subplots.

1.  **Row 1 (Main):** Candlestick + BB Upper/Lower + EMA 20/50.
2.  **Row 2 (RSI):** Line chart + Horizontal lines at 70 and 30.
3.  **Row 3 (MACD):** Histogram + Signal lines.

**Interaction:**

  * `grid.on('cellClicked', load_chart)`
  * The `load_chart` function queries DuckDB for the full history of the selected ticker and updates the Plotly figure via `ui.plotly.update()`.

## 7\. Implementation Roadmap

### Phase 1: Data Plumbing

1.  Create `market_data.duckdb`.
2.  Implement `ingest.py` with `yfinance`/OpenBB.
3.  **Test:** Run ingest, then run `duckdb market_data.duckdb "SELECT * FROM scanner_matrix LIMIT 5"` to verify data integrity.

### Phase 2: The Grid

1.  Initialize `main.py` with NiceGUI.
2.  Connect to DuckDB.
3.  Render `ui.aggrid` with data from `scanner_matrix` view.
4.  Implement the conditional class rules (Red/Green styling).

### Phase 3: The Charts

1.  Create `modules/charts.py` containing the `create_confluence_chart(df)` function.
2.  Wire up the Grid click event to the Chart update.

### Phase 4: Auto-Refresh

1.  Add a `ui.timer` to refresh the Grid every 60 seconds (reading from DB).
2.  Configure `ingest.py` to run as a background thread or separate cron job.
