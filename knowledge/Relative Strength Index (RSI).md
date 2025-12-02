---
tags:
  - technical-analysis
  - indicators
  - momentum
  - oscillators
aliases:
  - RSI
  - Relative Strength
created: 2025-11-26
---
# Relative Strength Index (RSI)

> [!INFO] Metadata
> * **Category:** Technical Analysis > Momentum Oscillators
> * **Developer:** J. Welles Wilder
> * **Standard Setting:** 14 Periods

---

## 1. Core Concept: Momentum & Velocity
The RSI is a momentum oscillator that measures the **speed** (velocity) and **change** (magnitude) of price movements.
* It is **bound** between 0 and 100.
* It focuses on the *rate of change* (deltas), not the absolute price value.


> [!NOTE] 🧠 Mental Model: The Car Speedometer
> Imagine the stock price is a car driving on a highway.
> * **The Price** = The car's GPS location (e.g., Mile Marker 150).
> * **The RSI** = The Speedometer (e.g., 80 mph).
>
> If the driver slams on the gas, the speedometer (RSI) spikes. If the driver eases off the gas, the speedometer (RSI) drops, *even if the car is still moving forward*.
>
> **Key Insight:** RSI tells us about acceleration and deceleration, not just direction.

---

## 2. The Calculation (The Engine)
RSI uses a two-step calculation based on the comparisons of "Average Gains" vs. "Average Losses" over a specific lookback period (usually 14).

### The Formula
**Step 1: Relative Strength (RS)**
$$RS = \frac{\text{Average Gain over 14 periods}}{\text{Average Loss over 14 periods}}$$

**Step 2: The Index (Normalization)**
$$RSI = 100 - \frac{100}{1 + RS}$$

> [!TIP] 🧠 Mental Model: The 14-Round Boxing Match
> View the last 14 candles as 14 rounds of boxing.
> * **Bulls (Buyers)** land punches on Green days.
> * **Bears (Sellers)** land punches on Red days.
>
> **The RS Calculation** asks: *Who hit harder on average?*
> If Bulls land massive knockouts and Bears only land weak jabs, the RSI approaches 100.
> * **Volatility Sensitivity:** A single massive candle (knockout punch) in the 14th round can drastically swing the average.

---

## 3. Interpretation: Overbought vs. Oversold
These levels indicate extreme momentum conditions where the price may be extended.

| Level | State | Implication |
| :--- | :--- | :--- |
| **> 70** | **Overbought** | Buying momentum is extreme. Price is "expensive" relative to recent moves. Potential for pullback. |
| **< 30** | **Oversold** | Selling momentum is extreme. Price is "cheap" relative to recent moves. Potential for bounce. |
| **50** | **Neutral** | Equilibrium between buyers and sellers. |

> [!WARNING] 🧠 Mental Model: The Rubber Band
> Think of price as a rubber band attached to a center pole (Fair Value).
> * **RSI 70/30:** The rubber band is stretched tight. There is high "potential energy" for it to snap back.
> * **The Trap:** A rubber band can *stay* stretched for a long time if the force pulling it (the trend) is strong enough. **Do not short just because RSI > 70.**

---

## 4. RSI Divergence (The Primary Signal)
Divergence occurs when the **Price Action** and the **RSI (Momentum)** disagree. This is a leading indicator of a reversal.


### A. Bearish Divergence (Top Reversal)
* **Price:** Makes a **Higher High** (HH) ↗️
* **RSI:** Makes a **Lower High** (LH) ↘️
* **Meaning:** The price is rising, but the buyers are exhausted.

### B. Bullish Divergence (Bottom Reversal)
* **Price:** Makes a **Lower Low** (LL) ↘️
* **RSI:** Makes a **Higher Low** (HL) ↗️
* **Meaning:** The price is falling, but the sellers are running out of steam.

> [!NOTE] 🧠 Mental Model: The Coasting Car
> * **Bearish Divergence:** The car is rolling up a hill (Higher Highs), but the driver has taken their foot off the gas (Lower RSI). Gravity will soon take over, and the car will roll back.
> * **Bullish Divergence:** The car is rolling down a hill, but the driver is slamming the brakes (RSI rising). The car will soon stop.

---

## 5. Strategic Confluence (The Safety Valve)
**Never trade RSI in isolation.** It is a secondary confirmation tool.

* **Weak Signal:** "RSI is at 30." (Catching a falling knife).
* **Strong Signal:** "Price hit a multi-year Support Level **AND** RSI is showing Bullish Divergence."