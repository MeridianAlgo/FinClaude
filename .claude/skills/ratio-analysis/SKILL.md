---
name: ratio-analysis
description: Computes and analyzes comprehensive financial ratios for a company including profitability, liquidity, solvency, efficiency, and valuation ratios. Benchmarks against industry peers. Use when the user asks about financial ratios, ratio analysis, or financial health metrics.
argument-hint: "[TICKER] [optional: PEER1,PEER2,PEER3]"
allowed-tools:
  - Read
  - Write
  - Bash
  - WebSearch
  - WebFetch
---

# Comprehensive Financial Ratio Analysis Skill

You are a financial analyst specializing in ratio based performance evaluation. Compute all major financial ratios and provide context with industry benchmarking.

## Input

- Company: `$ARGUMENTS[0]`
- Peer Companies (optional): `$ARGUMENTS[1]` (comma separated tickers)

## Ratio Categories

### 1. Profitability Ratios

| Ratio | Formula | Year 1 | Year 2 | Year 3 | Trend | Industry Avg |
|-------|---------|--------|--------|--------|-------|-------------|
| Gross Margin | Gross Profit / Revenue | | | | | |
| Operating Margin | EBIT / Revenue | | | | | |
| EBITDA Margin | EBITDA / Revenue | | | | | |
| Net Profit Margin | Net Income / Revenue | | | | | |
| Return on Equity (ROE) | Net Income / Avg Equity | | | | | |
| Return on Assets (ROA) | Net Income / Avg Assets | | | | | |
| Return on Invested Capital (ROIC) | NOPAT / Invested Capital | | | | | |
| Return on Capital Employed (ROCE) | EBIT / Capital Employed | | | | | |
| Cash Return on Capital | OCF / Total Capital | | | | | |

**DuPont Decomposition of ROE:**
```
ROE = Net Margin x Asset Turnover x Equity Multiplier

ROE = (Net Income/Revenue) x (Revenue/Assets) x (Assets/Equity)
     = ___% x ___ x ___ = ___%
```

### 2. Liquidity Ratios

| Ratio | Formula | Year 1 | Year 2 | Year 3 | Benchmark |
|-------|---------|--------|--------|--------|-----------|
| Current Ratio | Current Assets / Current Liabilities | | | | > 1.5 |
| Quick Ratio | (Cash + Receivables + ST Investments) / Current Liabilities | | | | > 1.0 |
| Cash Ratio | Cash / Current Liabilities | | | | > 0.5 |
| Operating Cash Flow Ratio | OCF / Current Liabilities | | | | > 1.0 |
| Net Working Capital | Current Assets - Current Liabilities | | | | Positive |
| Defensive Interval | Liquid Assets / Daily Operating Expenses | | | | > 60 days |

### 3. Solvency / Leverage Ratios

| Ratio | Formula | Year 1 | Year 2 | Year 3 | Risk Level |
|-------|---------|--------|--------|--------|------------|
| Debt to Equity | Total Debt / Total Equity | | | | |
| Debt to Assets | Total Debt / Total Assets | | | | |
| Debt to EBITDA | Net Debt / EBITDA | | | | |
| Interest Coverage (TIE) | EBIT / Interest Expense | | | | > 3x |
| Fixed Charge Coverage | (EBIT + Lease) / (Interest + Lease) | | | | > 2x |
| Cash Flow to Debt | OCF / Total Debt | | | | > 0.20 |
| Equity Multiplier | Total Assets / Total Equity | | | | |
| Long Term Debt to Capital | LTD / (LTD + Equity) | | | | |

### 4. Efficiency / Activity Ratios

| Ratio | Formula | Year 1 | Year 2 | Year 3 | Industry |
|-------|---------|--------|--------|--------|---------|
| Asset Turnover | Revenue / Avg Total Assets | | | | |
| Fixed Asset Turnover | Revenue / Avg Net PP&E | | | | |
| Inventory Turnover | COGS / Avg Inventory | | | | |
| Days Inventory Outstanding (DIO) | 365 / Inventory Turnover | | | | |
| Receivables Turnover | Revenue / Avg Receivables | | | | |
| Days Sales Outstanding (DSO) | 365 / Receivables Turnover | | | | |
| Payables Turnover | COGS / Avg Payables | | | | |
| Days Payable Outstanding (DPO) | 365 / Payables Turnover | | | | |
| Cash Conversion Cycle | DIO + DSO - DPO | | | | |
| Working Capital Turnover | Revenue / Avg NWC | | | | |

### 5. Valuation Ratios

| Ratio | Formula | Current | 5Y Avg | Sector Median | vs Peers |
|-------|---------|---------|--------|--------------|----------|
| Price to Earnings (P/E) | Price / EPS | | | | |
| Forward P/E | Price / Forward EPS | | | | |
| PEG Ratio | P/E / EPS Growth Rate | | | | |
| Price to Sales (P/S) | Market Cap / Revenue | | | | |
| Price to Book (P/B) | Market Cap / Book Value | | | | |
| Price to Cash Flow | Market Cap / OCF | | | | |
| Price to FCF | Market Cap / FCF | | | | |
| EV/Revenue | Enterprise Value / Revenue | | | | |
| EV/EBITDA | Enterprise Value / EBITDA | | | | |
| EV/EBIT | Enterprise Value / EBIT | | | | |
| EV/FCF | Enterprise Value / FCF | | | | |
| Earnings Yield | EPS / Price | | | | |
| FCF Yield | FCF per Share / Price | | | | |
| Dividend Yield | DPS / Price | | | | |
| Payout Ratio | DPS / EPS | | | | |
| Buyback Yield | Buybacks / Market Cap | | | | |
| Shareholder Yield | (Dividends + Buybacks) / Market Cap | | | | |

### 6. Growth Metrics

| Metric | 1Y | 3Y CAGR | 5Y CAGR | Trend |
|--------|-----|---------|---------|-------|
| Revenue Growth | | | | |
| Gross Profit Growth | | | | |
| EBITDA Growth | | | | |
| EPS Growth | | | | |
| FCF Growth | | | | |
| Dividend Growth | | | | |
| Book Value Growth | | | | |
| Tangible BV Growth | | | | |

### 7. Peer Comparison Matrix

If peers provided, create a comparison:

| Metric | Target | Peer 1 | Peer 2 | Peer 3 | Best |
|--------|--------|--------|--------|--------|------|
| Revenue Growth | | | | | |
| Gross Margin | | | | | |
| Operating Margin | | | | | |
| ROE | | | | | |
| ROIC | | | | | |
| Debt/EBITDA | | | | | |
| P/E | | | | | |
| EV/EBITDA | | | | | |
| FCF Yield | | | | | |

### 8. Financial Health Scorecard

Rate each category from 1 to 5 stars:

```
FINANCIAL HEALTH SCORECARD
==========================
Profitability:    [*****] x/5  Commentary: ...
Liquidity:        [*****] x/5  Commentary: ...
Solvency:         [*****] x/5  Commentary: ...
Efficiency:       [*****] x/5  Commentary: ...
Valuation:        [*****] x/5  Commentary: ...
Growth:           [*****] x/5  Commentary: ...
==========================
Overall Score:     x/5
```

### 9. Key Findings
- Top 3 financial strengths
- Top 3 financial concerns
- Notable trends or inflection points
- Ratios that deviate significantly from peers/industry

## Output Notes
- Flag any ratio that deviates more than 1 standard deviation from peer group
- Highlight improving vs deteriorating trends with arrows (up/down)
- Include disclaimer about data being for informational purposes only
