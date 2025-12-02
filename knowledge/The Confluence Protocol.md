---
tags:
  - system
  - master-note
  - checklists
  - execution
aliases:
  - The Trinity Strategy
  - Master Setup
created: 2025-11-26
---

# The Complete Trading System: The "Confluence" Protocol

> [!SUMMARY] Goal
> To identify high-probability trades by stacking evidence (**Confluence**) and executing with strict mathematical safety.
> This system integrates **The Trinity** (Context), **Price Action** (Trigger), and **Risk Management** (Safety).

---

## Phase 0: The Regime (The Traffic Light)
*Before looking for signals, identify the market state using [[Average Directional Index (ADX)]].*

### 1. The Trend Filter (ADX)
* **The Question:** Are we Trending or Ranging?
* **The Logic:**
    *   **ADX > 25 (Trending):** Market has direction. **ONLY** take Trend Following / Breakout signals. **BLOCK** Mean Reversion.
    *   **ADX < 25 (Ranging):** Market is chopping. **ONLY** take Mean Reversion signals. **BLOCK** Breakouts.

---

## Phase 1: The Setup (The Landscape)
*Look for these conditions based on the Phase 0 Regime.*

### 1. [[Bollinger Bands]] (Volatility)
* **The Question:** Is the market squeezing or extended?
* **The Signal:**
    *   **The Squeeze (Trend Setup):** Bands are tight (Bandwidth low). Watch for a breakout.
    *   **The Extension (Reversion Setup):** Price is at the Upper/Lower Band. Watch for mean reversion.

### 2. [[MACD (Moving Average Convergence Divergence)|MACD]] (Trend Direction)
* **The Question:** Is the wind at my back?
* **The Signal:**
    *   **Bullish:** Line > Signal Line (Green Histogram).
    *   **Bearish:** Line < Signal Line (Red Histogram).
    *   **Zero Line:** Above 0 = Bull Market / Below 0 = Bear Market.

### 3. [[Relative Strength Index (RSI)|RSI]] (Momentum Health)
* **The Question:** Is the move healthy or exhausted?
* **The Signal:**
    *   **Divergence:** Price makes Highs, RSI makes Lows (Reversal Imminent).
    *   **Overbought/Oversold:** Watch for 70/30.
        *   *In Trends:* RSI > 70 confirms strength.
        *   *In Ranges:* RSI > 70 indicates a sell signal.

---

## Phase 2: The Trigger (Price Action)
*Do not enter until a specific candle confirms the Phase 1 thesis.*
*Reference:* [[Price Action - Candlestick Mastery]]

### Reversal Patterns (For Ranging Markets)
* **Hammer:** Long lower wick at Support (Bullish).
* **Shooting Star:** Long upper wick at Resistance (Bearish).
* **Engulfing:** A massive candle "swallows" the previous one (Momentum Shift).

### Continuation Patterns (For Trending Markets)
* **Marubozu:** A big solid candle breaking through a Bollinger Band Squeeze.

---

## Phase 3: The Execution (Risk Management)
*The mathematical safety net.*
*Reference:* [[Risk Management & Position Sizing]] & [[Average True Range (ATR)]]

### 1. Dynamic Stop Loss (ATR Trailing Stop)
* **Logic:** Use volatility to determine stop placement, avoiding random noise.
* **Calculation:**
    *   **Long:** $Stop = Entry - (Multiplier \times ATR)$
    *   **Short:** $Stop = Entry + (Multiplier \times ATR)$
*   *Standard Multiplier:* 2.0 to 3.0.

### 2. Position Sizing (The 1% Rule)
* **Rule:** Never risk more than **1% of Total Account Equity** on a single trade.
* **Formula:**
$$Shares = \frac{\text{Account Equity} \times 0.01}{|Entry - StopPrice|}$$

---

## Phase 4: System Configuration (Central Parameters)
*Default settings for the algorithmic engine. These are the "knobs" we tune.*

| Indicator | Parameter | Default Value | Purpose |
| :--- | :--- | :--- | :--- |
| **RSI** | Length | 14 | Momentum Lookback |
| **RSI** | OB/OS Thresholds | 70 / 30 | Reversion Triggers |
| **Bollinger** | Length | 20 | Volatility Baseline |
| **Bollinger** | Std Dev | 2.0 | Band Width |
| **MACD** | Fast / Slow / Sig | 12 / 26 / 9 | Trend Identification |
| **ADX** | Length | 14 | Trend Strength |
| **ADX** | Regime Threshold | 25 | Filter (Trend vs. Range) |
| **ATR** | Length | 14 | Volatility Measure |
| **ATR** | Stop Multiplier | 2.0 | Dynamic Stop Distance |

---

## ✅ The "Perfect Trade" Checklist
*If you cannot check all boxes, **DO NOT** take the trade.*

- [ ] **Regime:** Have I checked ADX? (Is it > 25 or < 25?)
- [ ] **Strategy Match:** Am I using the right strategy for the regime? (Trend vs. Reversion)
- [ ] **Context:** Is Price at a Key Level (Support/Resistance)?
- [ ] **Volatility:** Are [[Bollinger Bands]] showing a setup?
- [ ] **Momentum:** Is [[Relative Strength Index (RSI)|RSI]] confirming the move?
- [ ] **Trigger:** Did a proper Candle Pattern close?
- [ ] **Risk:** Is my Stop Loss set based on ATR?
- [ ] **Size:** Is my Position Size calculated to risk max 1%?
