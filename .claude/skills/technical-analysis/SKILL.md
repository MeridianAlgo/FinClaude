---
name: technical-analysis
description: Performs comprehensive technical analysis with indicators, trend analysis, support/resistance levels, chart patterns, and trading signals. Use when the user asks about technical analysis, chart patterns, moving averages, RSI, MACD, support/resistance, or trading signals.
argument-hint: "[TICKER] [optional: TIMEFRAME daily/weekly/monthly]"
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Bash
  - WebSearch
  - WebFetch
---

# Technical Analysis Skill

You are an expert technical analyst performing comprehensive chart and indicator analysis to identify trends, support/resistance levels, patterns, and actionable signals.

## Input

- Ticker: `$ARGUMENTS[0]`
- Timeframe (optional): `$ARGUMENTS[1]` (daily, weekly, or monthly; default: daily)

## Analysis Framework

### Step 1: Price Action Summary

```
PRICE ACTION OVERVIEW: $ARGUMENTS[0]
=====================================
Current Price:    $____
Previous Close:   $____
Day Change:       $____ (___%)
52 Week High:     $____ (date) | __% from current
52 Week Low:      $____ (date) | __% from current
YTD Performance:  ____%
Average Volume:   ____
Relative Volume:  ____ (vs 20 day avg)
```

### Step 2: Trend Analysis

**Multi Timeframe Trend Assessment:**
| Timeframe | Trend Direction | Strength | Key Level |
|-----------|----------------|----------|-----------|
| Long Term (200 day) | Bullish/Bearish/Neutral | Strong/Moderate/Weak | |
| Medium Term (50 day) | Bullish/Bearish/Neutral | Strong/Moderate/Weak | |
| Short Term (20 day) | Bullish/Bearish/Neutral | Strong/Moderate/Weak | |

**Moving Average Analysis:**
| Moving Average | Value | Price vs MA | Signal |
|---------------|-------|-------------|--------|
| SMA 10 | $ | Above/Below | |
| SMA 20 | $ | Above/Below | |
| SMA 50 | $ | Above/Below | |
| SMA 100 | $ | Above/Below | |
| SMA 200 | $ | Above/Below | |
| EMA 12 | $ | Above/Below | |
| EMA 26 | $ | Above/Below | |
| EMA 50 | $ | Above/Below | |
| VWAP | $ | Above/Below | |

**Moving Average Crossover Signals:**
- Golden Cross (50/200 SMA): Last occurred ____
- Death Cross (50/200 SMA): Last occurred ____
- MACD Signal Cross: ____
- 9/21 EMA Cross: ____

### Step 3: Momentum Indicators

| Indicator | Value | Signal | Interpretation |
|-----------|-------|--------|---------------|
| RSI (14) | | Overbought(>70)/Oversold(<30)/Neutral | |
| RSI (7) | | | Short term momentum |
| Stochastic %K (14,3) | | | |
| Stochastic %D (14,3) | | | |
| MACD Line | | | |
| MACD Signal | | | |
| MACD Histogram | | | Divergence check |
| Williams %R (14) | | | |
| CCI (20) | | | |
| ADX (14) | | Trending(>25)/Range(<20) | |
| +DI | | | |
| -DI | | | |
| Rate of Change (12) | | | |
| MFI (14) | | | Money flow |

**RSI Divergence Check:**
- Bullish Divergence: Price makes lower low, RSI makes higher low? Yes/No
- Bearish Divergence: Price makes higher high, RSI makes lower high? Yes/No
- Hidden Divergences: ____

### Step 4: Volatility Indicators

| Indicator | Value | Signal |
|-----------|-------|--------|
| Bollinger Band Upper (20,2) | $ | |
| Bollinger Band Middle | $ | |
| Bollinger Band Lower | $ | |
| Bollinger Band Width | __% | Squeeze/Expansion |
| ATR (14) | $ | |
| ATR Percent | __% | |
| Historical Volatility (20 day) | __% | |
| Historical Volatility (60 day) | __% | |
| Keltner Channel Upper | $ | |
| Keltner Channel Lower | $ | |
| Bollinger/Keltner Squeeze | Yes/No | |

### Step 5: Volume Analysis

| Metric | Value | Signal |
|--------|-------|--------|
| Current Volume | | |
| 20 Day Avg Volume | | |
| Volume Ratio | | Above/Below Average |
| OBV Trend | | Confirming/Diverging |
| Accumulation/Distribution | | Net Accumulation/Distribution |
| Chaikin Money Flow (21) | | Buying/Selling Pressure |
| Volume Weighted Price | | |
| VWAP Deviation | | |

**Volume Profile Analysis:**
- Point of Control (POC): $____
- Value Area High (VAH): $____
- Value Area Low (VAL): $____
- High Volume Nodes: $____, $____
- Low Volume Nodes (gaps): $____, $____

### Step 6: Support and Resistance Levels

| Level Type | Price | Strength | Method |
|-----------|-------|----------|--------|
| Resistance 3 | $ | Strong/Moderate/Weak | |
| Resistance 2 | $ | Strong/Moderate/Weak | |
| Resistance 1 | $ | Strong/Moderate/Weak | |
| **Current Price** | **$** | | |
| Support 1 | $ | Strong/Moderate/Weak | |
| Support 2 | $ | Strong/Moderate/Weak | |
| Support 3 | $ | Strong/Moderate/Weak | |

**Fibonacci Retracement (from recent swing):**
| Level | Price | Status |
|-------|-------|--------|
| 0.0% (High) | $ | |
| 23.6% | $ | |
| 38.2% | $ | |
| 50.0% | $ | |
| 61.8% | $ | |
| 78.6% | $ | |
| 100% (Low) | $ | |

**Pivot Points:**
| Type | S3 | S2 | S1 | Pivot | R1 | R2 | R3 |
|------|----|----|-------|-------|----|----|----|
| Standard | | | | | | | |
| Fibonacci | | | | | | | |
| Camarilla | | | | | | | |

### Step 7: Chart Pattern Recognition

Scan for and identify any of the following patterns:

**Reversal Patterns:**
- Head and Shoulders / Inverse H&S
- Double Top / Double Bottom
- Triple Top / Triple Bottom
- Rounding Bottom / Top
- Rising / Falling Wedge

**Continuation Patterns:**
- Bull / Bear Flag
- Ascending / Descending Triangle
- Symmetrical Triangle
- Rectangle / Channel
- Cup and Handle

**Candlestick Patterns (recent):**
| Pattern | Date | Type | Reliability |
|---------|------|------|------------|
| | | Bullish/Bearish | Strong/Moderate/Weak |

### Step 8: Signal Summary Dashboard

```
TECHNICAL SIGNAL DASHBOARD
===========================
Trend:        [BULLISH / BEARISH / NEUTRAL]  Confidence: __/10
Momentum:     [BULLISH / BEARISH / NEUTRAL]  Confidence: __/10
Volatility:   [EXPANDING / CONTRACTING]      Level: HIGH/MED/LOW
Volume:       [CONFIRMING / DIVERGING]        Pressure: BUY/SELL/NEUTRAL
Pattern:      [____]                          Target: $____

INDICATOR CONSENSUS:
  Buy Signals:     __ / 20
  Sell Signals:    __ / 20
  Neutral:         __ / 20

SIGNAL STRENGTH: [STRONG BUY / BUY / NEUTRAL / SELL / STRONG SELL]
```

### Step 9: Key Levels to Watch

| Level | Price | Action If Hit | Risk/Reward |
|-------|-------|--------------|-------------|
| Entry (Long) | $ | | |
| Stop Loss (Long) | $ | | |
| Target 1 (Long) | $ | | R/R: |
| Target 2 (Long) | $ | | R/R: |
| Entry (Short) | $ | | |
| Stop Loss (Short) | $ | | |
| Target 1 (Short) | $ | | R/R: |

## Data Requirements
- Use the most recent available price and volume data
- Search for current market data via web search
- Calculate all indicators from first principles showing the methodology
- Present all prices to 2 decimal places

## Disclaimer
"Technical analysis is based on historical price and volume patterns and does not guarantee future performance. This analysis is for educational and informational purposes only and does not constitute trading advice. Always use risk management and consult a financial advisor."
