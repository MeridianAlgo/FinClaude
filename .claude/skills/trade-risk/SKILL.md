---
name: trade-risk
description: Position-level risk assessment. Position sizing recommendations, VaR, drawdown scenarios, risk/reward, stop-loss levels, and a risk score. Use when the user wants risk analysis or runs /trade risk <TICKER>.
argument-hint: "<TICKER> [optional: PORTFOLIO_SIZE like 100000]"
allowed-tools:
  - WebSearch
  - WebFetch
---

# /trade risk — Risk Assessment & Position Sizing

You are a risk manager providing position-level risk analysis for `$ARGUMENTS[0]`.

## Ticker: `$ARGUMENTS[0]`
## Portfolio Size (optional): `$ARGUMENTS[1]` (default: $100,000)

---

## Step 1: Risk Profile Overview

```
RISK PROFILE — [TICKER]
════════════════════════════════════════
Risk Score:           __/100 (higher = riskier)
Risk Level:           [LOW / MODERATE / ELEVATED / HIGH / EXTREME]
Beta (vs S&P 500):    ____
Annualized Volatility: ____%
Max Historical DD:    ___% (period: ____)
Current Drawdown:     ____%
Implied Volatility:   ___% (IVR: ___%)
```

---

## Step 2: Volatility Analysis

| Metric | Value | vs S&P 500 | Interpretation |
|--------|-------|-----------|----------------|
| Daily Volatility | ___% | | |
| Annual Volatility | ___% | | |
| Beta | | 1.00 | |
| IV (30D) | ___% | | |
| IV Rank | ___% | | |
| Realized vs Implied | | | |

**Volatility Regime:** Low (<15%) / Normal (15-30%) / Elevated (30-50%) / Extreme (>50%)

---

## Step 3: Value at Risk

Calculated on a $100,000 (or user-provided) position:

| Method | 95% VaR (1D) | 99% VaR (1D) | 95% VaR (10D) | 99% VaR (10D) |
|--------|-------------|-------------|--------------|--------------|
| Parametric | $____ (___%) | $____ | $____ | $____ |
| Historical | $____ (___%) | $____ | $____ | $____ |

**Expected Shortfall (CVaR 95%):** $____ — the average loss when things are really bad

---

## Step 4: Drawdown Analysis

**Historical Worst Drawdowns:**
| Rank | Period | Drawdown | Duration | Recovery |
|------|--------|----------|----------|----------|
| 1 | | ___% | __ days | __ days |
| 2 | | ___% | __ days | __ days |
| 3 | | ___% | __ days | __ days |

- Average max drawdown: ____%
- Average recovery time: ____ days
- Time underwater (% of history): ____%

---

## Step 5: Position Sizing Recommendations

Using multiple position-sizing frameworks:

**Kelly Criterion (approximate):**
- Estimated edge: ___% | Win rate: ___% | Avg win/loss: __
- Kelly %: ___% → Half-Kelly: ___% (recommended)

**Volatility-Adjusted Sizing (1% daily portfolio risk):**
- Position Size: $____ (__% of $100K portfolio)
- Shares: ____

**Fixed Fractional (2% of portfolio at risk):**
- Max loss per trade: $____ (2% of $100K)
- Suggested entry: $____ | Stop: $____
- Position size: $____ | Shares: ____

**ATR-Based Stop:**
- ATR (14D): $____
- 2×ATR stop: $____ below entry
- Position size for 2% risk: $____ | Shares: ____

**Recommended Position Size:**
| Portfolio % | Dollar Amount | Shares at $____ |
|-------------|--------------|-----------------|
| Conservative (1%) | $1,000 | |
| Moderate (2-3%) | $2,000-$3,000 | |
| Aggressive (5%) | $5,000 | |

---

## Step 6: Scenario Analysis

| Scenario | Portfolio Move | Dollar Impact (2% position) |
|----------|---------------|----------------------------|
| Stock +10% | | |
| Stock +20% | | |
| Stock -10% | | |
| Stock -20% | | |
| Stock -40% | | |
| S&P 500 -10% (beta adj.) | | |
| S&P 500 -25% (beta adj.) | | |
| Earnings miss (-15%) | | |

---

## Step 7: Stop Loss & Risk/Reward Levels

| Level Type | Price | % from Current | Method |
|------------|-------|---------------|--------|
| Tight Stop | $____ | -___% | 1×ATR |
| Moderate Stop | $____ | -___% | 2×ATR |
| Wide Stop | $____ | -___% | Key support |
| Target 1 | $____ | +___% | 2:1 R/R from tight stop |
| Target 2 | $____ | +___% | 3:1 R/R |
| Full Bull Target | $____ | +___% | Thesis target |

---

## Step 8: Risk Score Dashboard

```
RISK DASHBOARD — [TICKER]
══════════════════════════════════════
Volatility Risk:    __/25  — Annualized vol ___%, Beta __
Drawdown Risk:      __/25  — Max DD ___%, Current DD ___%
Tail Risk:          __/25  — Fat tails, event risk, earnings
Liquidity Risk:     __/25  — Avg daily vol: __M shares
────────────────────────────────────
Risk Score:         __/100  [LOWER = SAFER]
Risk Grade:         [A=Low / B=Moderate / C=Elevated / D=High / F=Extreme]

RECOMMENDED ACTION:
  Max Position Size: __% of portfolio ($____)
  Stop Loss:         $____ (___% from current)
  Risk/Reward:       __:1 at $____ target
```

---

⚠️ Risk models are estimates based on historical data. Actual losses may exceed modeled VaR. For educational purposes only. Not financial advice.
