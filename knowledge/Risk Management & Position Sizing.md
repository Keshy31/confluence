---
tags:
  - risk-management
  - psychology
  - math
  - execution
aliases:
  - Position Sizing
  - The 1% Rule
created: 2025-11-26
---

# Risk Management & Position Sizing

> [!SUMMARY] Purpose
> To survive inevitable losing streaks and ensure long-term profitability.
> **Core Philosophy:** Trading is not about predicting the future; it is about managing the cost of being wrong.

---

## 1. The Math of Ruin (The Cost of Losses)
Losses work geometrically against you. If you lose a chunk of your capital, you need a *larger* percentage gain just to get back to even.

| Loss % | Gain Needed to Break Even |
| :--- | :--- |
| **10%** | 11% |
| **20%** | 25% |
| **50%** | **100%** |
| **90%** | **900%** |

> [!DANGER] The Lesson
> Protecting your "capital base" is more important than chasing big wins. Once you fall into the 50% hole, recovery becomes mathematically improbable.

---

## 2. The 1% Rule (The Shark Cage)
**Rule:** Never risk more than **1% to 2%** of your *total account balance* on a single trade entry.
* This refers to the **amount lost** if the Stop Loss is hit, not the total investment amount.
* **Survival:** At 1% risk, you would need to lose **100 trades in a row** to go bust.

---

## 3. The Risk/Reward Ratio (The Edge)
You do not need to win 90% of the time to be rich. You just need your winners to be bigger than your losers.

* **Target Ratio:** Minimum **1:2** or **1:3**.

### The Math of 1:3 (50% Win Rate)
* **5 Losers** @ $100 loss = -$500
* **5 Winners** @ $300 gain = +$1,500
* **Net Profit:** **+$1,000**
* *Result:* You can be wrong half the time and still make a fortune.

---
## 3.5. Advanced Sizing: The Kelly Criterion 🧠
*The theoretical upper limit of risk.*

While the 1% rule keeps you alive, the **Kelly Criterion** calculates the mathematically optimal bet size to maximize long-term wealth growth based on your edge.

$$Kelly \% = W - \frac{1 - W}{R}$$

* **W:** Win Rate (e.g., 0.50 for 50%).
* **R:** Win/Loss Ratio (e.g., 2.0 for 2:1 Reward/Risk).

**Example:**
* Win Rate: 50%
* R/R: 2:1
* **Kelly = $0.50 - \frac{0.50}{2} = 0.25$ (25% Risk!)**

> [!DANGER] The "Full Kelly" Trap
> "Full Kelly" suggests risking 25% of your account on one trade in the example above. This is **suicide** in the real world because:
> 1.  **Estimation Error:** Your Win Rate is a guess, not a fact.
> 2.  **Black Swans:** Markets have "fat tails" (crashes) that formulas miss.
>
> **The Solution:** Use **"Fractional Kelly"** (usually Half-Kelly or Quarter-Kelly).
> * *Elite Standard:* Calculate Kelly, then multiply by **0.25**. If that number is higher than your 1% rule, stick to 1%.

---

---

## 4. Position Sizing (The Formula)
*Never guess the number of shares. Calculate it.*

$$Position Size (Shares) = \frac{\text{Account Risk (\$)}}{\text{Entry Price} - \text{Stop Loss Price}}$$

**The Variables:**
1.  **Account Risk:** Total Equity $\times$ 0.01 (1%).
2.  **Entry Price:** Where you buy.
3.  **Stop Loss:** The technical invalidation point (e.g., below the Hammer wick or Support).

### 🧮 Example Calculation
* **Account:** $20,000
* **Risk (1%):** $200
* **Entry:** $180
* **Stop:** $170 (Risk per share = $10)

$$Shares = \frac{200}{10} = 20 \text{ Shares}$$

---

## 5. The Golden Rules
1.  **Stop Loss is Non-Negotiable:** It must be in the system *before* you press buy.
2.  **Don't Move the Goalpost:** Never widen your stop loss when the trade goes against you.
3.  **Earn the Right to Size Up:** Only increase your risk % after you have doubled your account.