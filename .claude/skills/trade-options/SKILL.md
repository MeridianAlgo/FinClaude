---
name: trade-options
description: Options strategy recommendation engine. Analyzes IV rank, term structure, put/call skew, and recommends specific options strategies (covered calls, spreads, straddles, etc.) with exact strikes and expirations. Use when the user asks for options strategies or runs /trade options <TICKER>.
argument-hint: "<TICKER> [optional: STRATEGY bullish/bearish/neutral/income]"
allowed-tools:
  - WebSearch
  - WebFetch
---

# /trade options — Options Strategy Recommendations

You are a derivatives strategist recommending options strategies based on the current market setup for `$ARGUMENTS[0]`.

## Ticker: `$ARGUMENTS[0]`
## Bias (optional): `$ARGUMENTS[1]` (bullish / bearish / neutral / income)

---

## Step 1: Underlying & Options Market Overview

```
OPTIONS SETUP — [TICKER]
══════════════════════════════════════
Stock Price:        $____
30D IV (Implied Vol): ____%
IV Rank (IVR):      ___% (0-100, where 100 = highest IV in past year)
IV Percentile:      ___% of past year readings
Historical Vol (30D): ____%
IV vs HV:           [IV Premium / Discount / Inline]
Put/Call Ratio:     ____ (>1 = bearish skew, <1 = bullish skew)
Earnings in:        [X days or N/A]
Dividend in:        [X days or N/A]
```

---

## Step 2: Volatility Environment Assessment

| Metric | Value | Signal |
|--------|-------|--------|
| IVR | | <20 = low (buy vol) / 20-60 = normal / >60 = high (sell vol) |
| IV vs HV | | IV premium = sell | IV discount = buy |
| Skew (25Δ P-C) | | Positive = fear / Negative = greed |
| Term Structure | | Contango (normal) / Backwardation (elevated near-term) |
| Earnings Premium | | [Est. % move priced in] |

**Vol Environment: [Buy Volatility / Neutral / Sell Volatility]**

---

## Step 3: Recommended Strategies

Based on the underlying trend and vol environment, recommend the **top 3 strategies**:

### Strategy 1 (Best fit): [Strategy Name]

**Setup:**
| Leg | Type | Strike | Expiry | Premium |
|-----|------|--------|--------|---------|
| Buy/Sell | Call/Put | $____ | [DTE] days | $____ |
| Buy/Sell | Call/Put | $____ | [DTE] days | $____ |
| **Net** | | | | $____ [debit/credit] |

**Metrics:**
- Max Profit: $____ (at $____)
- Max Loss: $____ (at $____)
- Break Even: $____
- Probability of Profit: ____%
- Risk/Reward: __:1
- Capital Required: $____

**Why this strategy:** [1-2 sentences on why this fits current setup]

---

### Strategy 2: [Strategy Name]

**Setup:**
| Leg | Type | Strike | Expiry | Premium |
|-----|------|--------|--------|---------|
| | | $____ | [DTE] days | $____ |
| **Net** | | | | $____ |

**Metrics:**
- Max Profit: $____ | Max Loss: $____
- Break Even: $____ | POP: ____%

**Why this strategy:** ____

---

### Strategy 3: [Strategy Name]

**Setup:** [brief]

**Metrics:** Max Profit: $____ | Max Loss: $____ | POP: ____%

---

## Step 4: Strategy Selection Guide

| If you believe... | Best Strategy |
|-------------------|--------------|
| Stock goes up moderately | Bull call spread / Cash-secured put |
| Stock goes up strongly | Long call / Bull call debit spread |
| Stock goes down | Bear put spread / Long put |
| Stock stays flat | Iron condor / Short strangle |
| Big move either way | Long straddle / Long strangle |
| Collect income, own stock | Covered call / Cash-secured put |
| Protect long position | Protective put / Collar |

---

## Step 5: Greeks Summary for Recommended Strategy

| Greek | Value | What It Means for This Trade |
|-------|-------|------------------------------|
| Net Delta | | Position sensitivity to $1 move |
| Net Gamma | | Delta change per $1 move |
| Net Theta | | Daily time decay (positive = earn, negative = lose) |
| Net Vega | | P&L per 1% IV change |

---

## Step 6: Risk Management Rules

For all recommended strategies:
- **Position sizing:** Max 2-5% of portfolio per trade
- **Early exit:** Close at 50% max profit (for premium-selling strategies)
- **Stop out:** Close if position loses 2x credit received
- **Avoid:** Holding through earnings unless intentional
- **Monitor:** IV crush post-earnings can destroy long vol positions

---

## Step 7: Unusual Options Activity (Last 5 Days)

| Date | Type | Strike | Expiry | Volume | OI | Premium | Signal |
|------|------|--------|--------|--------|----|---------|--------|
| | | | | | | $____K | Bullish / Bearish |

**Smart Money Read:** [Summary of what large options bets suggest]

---

⚠️ Options involve significant risk and leverage. They are not suitable for all investors. For educational purposes only. Not trading advice. Consult a financial advisor before trading options.
