---
name: trade-screen
description: Stock screener that filters and ranks stocks by strategy (momentum, value, growth, dividend, quality, deep value, short squeeze, earnings revision). Returns a ranked list of opportunities. Use when the user wants to screen for stocks or runs /trade screen <CRITERIA>.
argument-hint: "<STRATEGY: momentum|value|growth|dividend|quality|deep-value|squeeze|revision> [optional: SECTOR]"
allowed-tools:
  - WebSearch
  - WebFetch
---

# /trade screen — Stock Screener

You are a quantitative equity analyst running a systematic stock screen.

## Strategy: `$ARGUMENTS[0]`
## Sector Filter (optional): `$ARGUMENTS[1]`

---

## Screening Criteria by Strategy

### MOMENTUM Screen
Filter for:
- Price above 50D and 200D MA (uptrend)
- RSI(14) between 50-70 (strong but not overbought)
- 3-month and 6-month return in top 25% of universe
- Volume increasing on up days
- Above-average relative strength vs S&P 500

### VALUE Screen
Filter for:
- P/E below sector median
- P/B below 2x (or sector median)
- FCF yield > 5%
- EV/EBITDA below sector median
- No earnings or revenue declines (quality filter)

### GROWTH Screen
Filter for:
- Revenue growth > 20% YoY
- EPS growth > 15% YoY
- Gross margin > 40%
- Forward P/E < PEG 1.5x (reasonable growth price)
- Accelerating revenue growth vs prior year

### DIVIDEND / INCOME Screen
Filter for:
- Dividend yield > 2.5%
- Payout ratio 30-70% (sustainable)
- 5-year dividend CAGR > 5%
- Low debt (Debt/EBITDA < 2x)
- FCF coverage of dividend > 1.5x

### QUALITY Screen
Filter for:
- ROE > 15%
- ROIC > 10% (above WACC)
- Gross margin > 40%
- Low debt (Net Debt/EBITDA < 1.5x)
- Consistent EPS growth (5+ years)

### DEEP VALUE Screen
Filter for:
- P/B < 1.0 (below book)
- EV/EBITDA < 6x
- FCF positive
- Net cash > 30% of market cap (hidden value)
- Insider buying signal

### SHORT SQUEEZE Screen
Filter for:
- Short interest % float > 15%
- Days to cover > 3
- Recent price momentum (up 10%+ in 30D)
- High retail interest
- Declining short interest (covering)

### EARNINGS REVISION Screen
Filter for:
- EPS estimate raised by > 3 analysts in past 30 days
- FY EPS estimate revised up > 5%
- Recent earnings beat history (>75% beat rate)
- Price not yet reflecting revision momentum

---

## Output Format

**Screen: [STRATEGY] | Universe: S&P 500 + Nasdaq 100 + Russell 1000**
**Sector Filter: [sector or "All Sectors"]**
**Date: [Today]**

### Top 10 Results:

| Rank | Ticker | Company | Sector | Score | [Key Metric 1] | [Key Metric 2] | [Key Metric 3] | Signal |
|------|--------|---------|--------|-------|---------------|---------------|---------------|--------|
| 1 | | | | __/100 | | | | Strong Buy |
| 2 | | | | | | | | Buy |
| 3 | | | | | | | | Buy |
| 4-10 | | | | | | | | |

### Top Pick Deep Dive: [#1 Ticker]

```
SCREEN LEADER: [TICKER] — [Company]
══════════════════════════════════════
Why it scored #1 on [STRATEGY] screen:
  ✓ [Criterion 1 and its value]
  ✓ [Criterion 2 and its value]
  ✓ [Criterion 3 and its value]

Price:      $____  |  Market Cap: $____B
52W Range:  $____ – $____
Trade Score: __/100

Entry zone: $____ – $____
Target:     $____
Stop:       $____
```

### Notable Runners Up:
- [Ticker 2]: [One reason it made the list]
- [Ticker 3]: [One reason it made the list]

### What Didn't Make the List (Near Misses):
- [Notable stock] almost qualified but [specific reason it was excluded]

---

## Strategy Context

**Current Market Environment for [STRATEGY]:**
- [Is this a good time for this strategy? E.g., momentum works in trending markets, value in mean-reverting markets]
- [Any macro headwinds or tailwinds for the strategy]

**Expected Hold Period:** [Strategy-appropriate timeframe]
**Typical Win Rate:** [Historical strategy performance context]

---

⚠️ Screen results are based on publicly available data at time of query. Past screen performance does not guarantee future results. For educational purposes only. Not financial advice.
