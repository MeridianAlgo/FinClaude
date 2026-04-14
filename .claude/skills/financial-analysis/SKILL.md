---
name: financial-analysis
description: Performs deep fundamental financial analysis of a company. Use when the user asks to analyze a company, review financials, evaluate a stock, or understand a business's financial health. Covers income statements, balance sheets, cash flow statements, and trend analysis.
argument-hint: "[TICKER or COMPANY NAME]"
allowed-tools:
  - Read
  - Write
  - Bash
  - WebSearch
  - WebFetch
---

# Deep Financial Analysis Skill

You are an expert financial analyst performing an institutional grade fundamental analysis. When invoked, conduct a comprehensive financial deep dive.

## Input

The user will provide a company name or ticker symbol via `$ARGUMENTS`. If no argument is provided, ask the user which company to analyze.

**Target: $ARGUMENTS**

## Analysis Framework

### Step 1: Company Overview
- Full legal name, ticker, exchange, sector, and industry
- Market capitalization and enterprise value
- Business description and revenue segments
- Key executives and insider ownership
- Recent major events (mergers, acquisitions, restructurings)

### Step 2: Income Statement Analysis (3 to 5 years)
Present a table with the following line items:
| Metric | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | CAGR |
|--------|--------|--------|--------|--------|--------|------|
| Revenue | | | | | | |
| Cost of Revenue | | | | | | |
| Gross Profit | | | | | | |
| Gross Margin % | | | | | | |
| Operating Expenses | | | | | | |
| R&D Expense | | | | | | |
| SGA Expense | | | | | | |
| Operating Income (EBIT) | | | | | | |
| Operating Margin % | | | | | | |
| Interest Expense | | | | | | |
| Pre Tax Income | | | | | | |
| Net Income | | | | | | |
| Net Margin % | | | | | | |
| EPS (Basic) | | | | | | |
| EPS (Diluted) | | | | | | |
| Shares Outstanding | | | | | | |

Analyze:
- Revenue growth trajectory and sustainability
- Margin expansion or compression trends
- Operating leverage effects
- Earnings quality indicators
- One time items and adjustments

### Step 3: Balance Sheet Analysis
Present a table with:
| Metric | Year 1 | Year 2 | Year 3 | Change |
|--------|--------|--------|--------|--------|
| Cash and Equivalents | | | | |
| Short Term Investments | | | | |
| Accounts Receivable | | | | |
| Inventory | | | | |
| Total Current Assets | | | | |
| PP&E (Net) | | | | |
| Goodwill | | | | |
| Intangible Assets | | | | |
| Total Assets | | | | |
| Accounts Payable | | | | |
| Short Term Debt | | | | |
| Current Portion LTD | | | | |
| Total Current Liabilities | | | | |
| Long Term Debt | | | | |
| Total Liabilities | | | | |
| Total Equity | | | | |
| Book Value Per Share | | | | |

Analyze:
- Liquidity position (current ratio, quick ratio)
- Capital structure and leverage
- Asset quality and composition
- Working capital management
- Goodwill and intangible asset risk

### Step 4: Cash Flow Analysis
Present a table with:
| Metric | Year 1 | Year 2 | Year 3 | Trend |
|--------|--------|--------|--------|-------|
| Net Income | | | | |
| Depreciation & Amortization | | | | |
| Stock Based Compensation | | | | |
| Changes in Working Capital | | | | |
| Operating Cash Flow | | | | |
| Capital Expenditures | | | | |
| Free Cash Flow | | | | |
| FCF Margin % | | | | |
| Acquisitions | | | | |
| Investing Cash Flow | | | | |
| Debt Issuance (Repayment) | | | | |
| Share Repurchases | | | | |
| Dividends Paid | | | | |
| Financing Cash Flow | | | | |
| Net Change in Cash | | | | |

Analyze:
- Cash flow quality (OCF vs Net Income)
- Free cash flow generation consistency
- Capital allocation priorities
- Shareholder return programs
- Cash conversion cycle

### Step 5: Key Metrics Summary
Create a summary dashboard:

```
=== FINANCIAL HEALTH DASHBOARD ===
Profitability:   Revenue Growth: __% | Gross Margin: __% | Operating Margin: __% | Net Margin: __% | ROE: __% | ROA: __%
Liquidity:       Current Ratio: __ | Quick Ratio: __ | Cash Ratio: __
Leverage:        Debt/Equity: __ | Debt/EBITDA: __ | Interest Coverage: __
Efficiency:      Asset Turnover: __ | Inventory Turnover: __ | Receivables Turnover: __
Valuation:       P/E: __ | P/S: __ | P/B: __ | EV/EBITDA: __ | PEG: __
Cash Flow:       FCF Yield: __% | OCF/Net Income: __ | CapEx/Revenue: __%
```

### Step 6: Competitive Positioning
- Compare key metrics against 3 to 5 direct competitors
- Industry average benchmarking
- Moat analysis (brand, network effects, switching costs, cost advantages, scale)

### Step 7: Risk Factors
- Top 5 business risks
- Financial risks (debt covenants, refinancing risk, currency exposure)
- Regulatory and legal risks
- Competitive threats
- Macro sensitivity

### Step 8: Summary and Outlook
- Bull case / Base case / Bear case scenarios
- Key catalysts (upcoming product launches, regulatory decisions, earnings)
- Critical metrics to monitor going forward

## Output Format
- Use clean markdown tables for all financial data
- Use bullet points for qualitative analysis
- Bold key findings and notable outliers
- Include a disclaimer: "This analysis is for informational purposes only and does not constitute investment advice."
- Include data source attribution and date of analysis

## Data Sources
Search the web for the most recent financial data from:
- SEC EDGAR filings (10-K, 10-Q)
- Company investor relations pages
- Yahoo Finance, Google Finance
- Industry reports and analyst consensus
