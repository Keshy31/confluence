---
tags:
  - technical-analysis
  - indicators
  - trend
  - filters
aliases:
  - ADX
  - Average Directional Index
created: 2025-11-26
---
# Average Directional Index (ADX)

> [!INFO] Metadata
> * **Category:** Technical Analysis > Trend Strength
> * **Developer:** J. Welles Wilder
> * **Standard Setting:** 14 Periods

---

## 1. Core Concept: Trend Strength
The ADX measures the **strength** of a trend, regardless of its direction.
* It answers the question: *"Are we trending or are we ranging?"*
* It is often displayed with two companion lines: **+DI** (Positive Directional Indicator) and **-DI** (Negative Directional Indicator), which determine the direction.

> [!NOTE] 🧠 Mental Model: The Gas Pedal
> * **Price Direction (+DI/-DI)** = The Steering Wheel (Left or Right).
> * **ADX** = The Gas Pedal (Speed).
>
> You can have the steering wheel turned sharply (Strong Directional signal), but if the gas pedal isn't pressed (Low ADX), the car won't go anywhere. **ADX confirms if the market has enough "gas" to sustain a move.**

---

## 2. Interpretation: The Traffic Light

| ADX Value | Regime | Strategy Implication |
| :--- | :--- | :--- |
| **< 20-25** | **Weak / Ranging** | **Mean Reversion.** Buy support, sell resistance. Avoid breakouts (they will likely fail). |
| **> 25** | **Trending** | **Trend Following.** Buy breakouts, sell breakdowns. Avoid fading moves (the train will run you over). |
| **> 50** | **Extreme Trend** | **Profit Taking.** The trend is very strong but may be overheating. Tighten stops. |

---

## 3. The Components (+DI / -DI)
While ADX is non-directional, its components tell you who is in control.

* **+DI (Green Line):** Measures strength of upward moves.
* **-DI (Red Line):** Measures strength of downward moves.

### The Crossover Signal
* **Buy Signal:** +DI crosses **above** -DI (Bulls take control).
* **Sell Signal:** -DI crosses **above** +DI (Bears take control).
* **Filter:** Only take the crossover signal if **ADX > 20** (The trend has strength).

---

## 4. Strategic Application (The Regime Filter)
The most powerful use of ADX is not as an entry trigger, but as a **Regime Filter** to choose *which* strategy to deploy.

### Scenario A: The Chop (ADX < 25)
* **Market State:** Sideways, noisy, oscillating.
* **Active Strategy:** **Mean Reversion** (e.g., Bollinger Band bounces, RSI overbought/oversold).
* **Blocked Strategy:** Breakouts.

### Scenario B: The Run (ADX > 25)
* **Market State:** Strong directional movement.
* **Active Strategy:** **Trend Following** (e.g., MACD crossovers, Breakouts).
* **Blocked Strategy:** Mean Reversion (RSI 70 is no longer a sell signal; it's a momentum confirmation).

> [!WARNING] The Lag
> ADX is a smoothed derivative of price. It lags significantly. It will not catch the *exact* top or bottom. It confirms the "meat" of the move. Do not use it for sniper entries.

