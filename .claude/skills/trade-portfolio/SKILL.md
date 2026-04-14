---
name: trade-portfolio
description: Portfolio analysis — correlation matrix, sector/factor exposure, concentration risk, performance attribution, and rebalancing recommendations. Accepts a list of tickers and optional weights. Use when the user asks for portfolio analysis or runs /trade portfolio.
argument-hint: "[TICKER1:WEIGHT%,TICKER2:WEIGHT%,...] [optional: BENCHMARK SPY/QQQ]"
allowed-tools:
  - WebSearch
  - WebFetch
---

# /trade portfolio — Portfolio Analysis

You are a portfolio risk manager analyzing a multi-asset portfolio.

## Holdings: `$ARGUMENTS[0]`
## Benchmark (optional): `$ARGUMENTS[1]` (default: SPY)

If no holdings provided, ask the user to input their tickers and optional weights (e.g., "AAPL:30,MSFT:20,GOOGL:15,AMZN:15,NVDA:20").

---

## Step 1: Portfolio Overview

```
PORTFOLIO OVERVIEW
════════════════════════════════════
Holdings:         [N] positions
Benchmark:        [SPY / QQQ / custom]
Total Value:      $____ (if provided, else % weights)
Data Period:      Last 1 year daily returns
```

**Holdings Table:**
| Ticker | Name | Weight % | 1Y Return | Volatility | Beta | Sector |
|--------|------|----------|-----------|------------|------|--------|
| | | | | | | |
| **Portfolio** | | 100% | | | | |
| **Benchmark** | SPY | - | | | 1.00 | |

---

## Step 2: Portfolio Performance Summary

| Period | Portfolio | Benchmark | Alpha | Notes |
|--------|-----------|-----------|-------|-------|
| 1 Month | | | | |
| 3 Months | | | | |
| 6 Months | | | | |
| YTD | | | | |
| 1 Year | | | | |

**Risk-Adjusted Performance:**
| Metric | Portfolio | Benchmark |
|--------|-----------|-----------|
| Annualized Return | | |
| Annualized Volatility | | |
| Sharpe Ratio | | |
| Sortino Ratio | | |
| Max Drawdown | | |
| Calmar Ratio | | |
| Beta | | 1.00 |
| Alpha (Jensen's) | | 0 |

---

## Step 3: Correlation Matrix

Display pairwise correlations between all holdings:

| | [T1] | [T2] | [T3] | [T4] | [T5] | SPY |
|--|------|------|------|------|------|-----|
| [T1] | 1.00 | | | | | |
| [T2] | | 1.00 | | | | |
| [T3] | | | 1.00 | | | |
| SPY | | | | | | 1.00 |

**High Correlation Pairs (>0.75) — Concentration Risk:**
- [Ticker1] ↔ [Ticker2]: __ — [Comment]

**Low/Negative Correlation Pairs — Diversification:**
- [Ticker1] ↔ [Ticker2]: __ — [Comment]

---

## Step 4: Sector & Factor Exposure

**Sector Concentration:**
| Sector | Weight % | Benchmark % | Over/Under |
|--------|----------|-------------|------------|
| Technology | | | |
| Healthcare | | | |
| Financials | | | |
| Consumer Discretionary | | | |
| [Other] | | | |

**Factor Exposures (vs benchmark):**
| Factor | Portfolio Tilt | Signal |
|--------|---------------|--------|
| Growth vs Value | | Tilted toward ____ |
| Large vs Small Cap | | |
| Quality | | |
| Momentum | | |
| Low Volatility | | |
| Dividend / Income | | |

---

## Step 5: Concentration & Risk Analysis

**Concentration Metrics:**
- Top holding weight: ___% [Ticker]
- Top 3 holdings: ___% of portfolio
- Herfindahl-Hirschman Index (HHI): ____ (>2,500 = concentrated)
- Effective number of holdings: ____ (diversification equivalent)

**Portfolio VaR:**
| Confidence | 1-Day VaR | 10-Day VaR |
|------------|-----------|------------|
| 95% | $____ | $____ |
| 99% | $____ | $____ |

**Stress Tests:**
| Scenario | Portfolio Impact | Benchmark | Relative |
|----------|-----------------|-----------|---------|
| 2022 Rate Shock (-25%) | | | |
| COVID Crash (-34%) | | | |
| 2008 GFC (-50%) | | | |
| Rate spike +200bps | | | |

---

## Step 6: Performance Attribution

**What drove portfolio returns vs benchmark:**
| Attribution Source | Contribution |
|-------------------|-------------|
| Selection (picking right stocks) | [+/-]___% |
| Allocation (sector weights) | [+/-]___% |
| Interaction effect | [+/-]___% |
| Total Active Return | [+/-]___% |

**Top Contributors (YTD):**
| Ticker | Weight | Return | Contribution |
|--------|--------|--------|-------------|
| | | | |

**Top Detractors (YTD):**
| Ticker | Weight | Return | Contribution |
|--------|--------|--------|-------------|
| | | | |

---

## Step 7: Rebalancing Recommendations

**Current vs Target Analysis:**
| Ticker | Current Weight | Recommended Target | Action |
|--------|--------------|-------------------|--------|
| | | | Trim / Hold / Add |

**Rebalancing Rationale:**
1. [Over-concentrated positions to reduce]
2. [Underrepresented exposures to add]
3. [High-correlation pairs to diversify]
4. [Suggested additions for diversification]

**Suggested Additions:**
| Ticker | Reason | Target Weight |
|--------|--------|--------------|
| | | |

---

## Step 8: Portfolio Scorecard

```
PORTFOLIO HEALTH — SCORECARD
══════════════════════════════════════
Diversification:   __/25  — [__ holdings, HHI __, sector spread]
Risk-Adjusted:     __/25  — [Sharpe __, Sortino __, Beta __]
Concentration:     __/25  — [Top holding ___%, High-corr pairs: __]
Momentum:          __/25  — [Portfolio alpha: [+/-]___% vs benchmark]
────────────────────────────────────
Portfolio Score:   __/100

OVERALL GRADE: [A/B/C/D]
Key Action: [Top 1 recommendation to improve portfolio]
```

---

⚠️ Portfolio analysis is based on historical data. Past performance does not guarantee future results. For educational purposes only. Not financial advice.
