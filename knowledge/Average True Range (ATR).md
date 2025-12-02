---
tags:
  - technical-analysis
  - indicators
  - volatility
  - risk-management
aliases:
  - ATR
  - Average True Range
created: 2025-11-26
---
# Average True Range (ATR)

> [!INFO] Metadata
> * **Category:** Technical Analysis > Volatility
> * **Developer:** J. Welles Wilder
> * **Standard Setting:** 14 Periods

---

## 1. Core Concept: Measuring the "Noise"
The ATR is a volatility indicator that measures the **magnitude** of price movement. It does **not** indicate direction.
* It tells you "how much" an asset typically moves in a given period (candle).
* Ideally used for **Risk Management** (Stop Losses) and **Position Sizing**, rather than entry signals.

> [!NOTE] 🧠 Mental Model: The Breathing Room
> Imagine a runner on a track.
> * **The Price** = The runner's current position.
> * **The ATR** = The length of the runner's stride.
>
> If the runner typically has a 1-meter stride (ATR = 1), setting a hurdle 0.5 meters away is foolish—they will trip over it randomly. You need to place obstacles (Stop Losses) outside their natural stride length.

---

## 2. The Calculation (The Ruler)
ATR accounts for gaps between candles, which simple "High minus Low" calculations miss.

### Step 1: True Range (TR)
The "True Range" is the **greatest** of the following three values:
1.  **Current High - Current Low** (Standard range)
2.  **|Current High - Previous Close|** (Accounts for gaps up)
3.  **|Current Low - Previous Close|** (Accounts for gaps down)

### Step 2: The Average
The ATR is simply the smoothed moving average (usually 14 periods) of the True Range values.

---

## 3. Interpretation: Volatility Regimes

| ATR Value | State | Implication |
| :--- | :--- | :--- |
| **Rising** | **High Volatility** | Price is moving aggressively. Candles are large. Stops need to be wider. |
| **Falling** | **Low Volatility** | Price is consolidating or drifting. Candles are small. Stops can be tighter. |

> [!WARNING] 🧠 Mental Model: The Weather Report
> * **High ATR** = Stormy Weather. Big waves. Do not use a small boat (tight stop).
> * **Low ATR** = Calm Seas. Small ripples. You can use a smaller boat (tight stop).

---

## 4. Strategic Application (The Edge)

### A. Dynamic Stop Losses (Chandelier Exit)
Instead of a fixed % stop (e.g., "sell if down 1%"), use an ATR-based stop to adapt to the asset's current behavior.
* **Long Stop:** $Entry - (k \times ATR)$
* **Short Stop:** $Entry + (k \times ATR)$
* *Common Multiplier (k):* 2.0 to 3.0.

### B. Position Sizing (Volatility Normalization)
Adjust your bet size based on volatility.
* **High Volatility (High ATR):** Buy **fewer** shares. (Risk per share is high).
* **Low Volatility (Low ATR):** Buy **more** shares. (Risk per share is low).
* This ensures your total dollar risk remains constant regardless of market conditions.

---

## 5. Confluence
* **Breakout Validation:** A breakout accompanied by a **rising ATR** suggests conviction and genuine momentum. A breakout with flat/falling ATR is likely a "fakeout."

