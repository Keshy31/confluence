---
tags:
  - technical-analysis
  - indicators
  - trend-following
  - momentum
aliases:
  - MACD
  - Moving Average Convergence Divergence
created: 2025-11-26
---

# MACD (Moving Average Convergence Divergence)

> [!INFO] Metadata
> * **Category:** Technical Analysis > Trend-Following Momentum
> * **Developer:** Gerald Appel
> * **Standard Setting:** 12, 26, 9

---

## 1. Core Concept: Trend & Direction
Unlike RSI (which is bound 0-100), MACD is **unbound**. It tracks the relationship between two moving averages to determine trend direction and strength.
* **Positive MACD:** Upside Momentum (Trend is Bullish).
* **Negative MACD:** Downside Momentum (Trend is Bearish).

> [!NOTE] 🧠 Mental Model: The Dog Walker
> * **The Slow Line (26 EMA)** = The **Walker** (The long-term trend).
> * **The Fast Line (12 EMA)** = The **Dog** (The short-term price).
>
> **The Interaction:**
> * The dog runs away (Divergence) -> Trend is strong.
> * The dog gets tired and waits for the walker (Convergence) -> Trend is slowing.
> * The dog crosses the walker -> **Trend Reversal**.

---

## 2. The Components



[Image of MACD indicator with MACD line signal line and histogram labeled]


### A. The MACD Line (The Gap)
$$MACD = \text{12 Period EMA} - \text{26 Period EMA}$$
* This calculates the "Distance" between the Dog and the Walker.

### B. The Signal Line (The Trigger)
* A 9-period EMA of the MACD Line itself.
* Think of this as the "average speed" of the Dog.

### C. The Histogram (The Visualizer)
* Represents the distance between the **MACD Line** and the **Signal Line**.
* **Green Bars:** MACD is above Signal (Bullish).
* **Red Bars:** MACD is below Signal (Bearish).

---

## 3. Signals

### The Crossover (The Main Trigger)
1.  **Bullish Cross:** MACD crosses **ABOVE** the Signal Line.
    * *Action:* Buy / Long.
2.  **Bearish Cross:** MACD crosses **BELOW** the Signal Line.
    * *Action:* Sell / Short.

### The Zero Line Cross (The Big Trend)
1.  **Crossing Above Zero:** The short-term average (12) is now higher than the long-term average (26). The "tide" has turned bullish.
2.  **Crossing Below Zero:** The "tide" has turned bearish.

---

## 4. Strategy: The RSI + MACD Combo
RSI is the **Scout**; MACD is the **Heavy Infantry**.

| Step  | Indicator | Condition      | Meaning                                                        |
| :---- | :-------- | :------------- | :------------------------------------------------------------- |
| **1** | **RSI**   | **Divergence** | "Momentum is changing, but price hasn't turned yet." (Warning) |
| **2** | **MACD**  | **Crossover**  | "The trend has officially confirmed the turn." (Trigger)       |

> [!TIP] Pro Tip regarding Timing
> RSI signals usually happen *before* MACD signals. Use RSI to build a "Watchlist" and MACD to push the "Buy Button."