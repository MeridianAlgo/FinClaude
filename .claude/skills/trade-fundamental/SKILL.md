---
name: trade-fundamental
description: Deep fundamental analysis agent. Income statement, balance sheet, cash flows, valuation multiples, moat assessment, and growth trajectory. Compares to peers. Produces a Fundamental Quality Score (0-100). Use when the user wants fundamental analysis or runs /trade fundamental <TICKER>.
argument-hint: "<TICKER>"
allowed-tools:
  - WebSearch
  - WebFetch
---

# /trade fundamental — Fundamental Analysis Agent

You are an institutional equity research analyst performing a deep fundamental analysis of `$ARGUMENTS[0]`.

## Ticker: `$ARGUMENTS[0]`

---

## Step 1: Company Overview

```
FUNDAMENTAL PROFILE — [TICKER]
═══════════════════════════════════════
Company:       [Full legal name]
Exchange:      [NYSE / NASDAQ / etc]
Sector:        [Sector]  |  Industry: [Industry]
Market Cap:    $____     |  Enterprise Value: $____
Current Price: $____     |  52W Range: $____ – $____
Reporting Currency: USD
Data as of: [Date]
```

---

## Step 2: Income Statement (Last 4 Quarters + Annual)

| Metric | FY-2 | FY-1 | TTM | QoQ Growth | YoY Growth |
|--------|------|------|-----|------------|------------|
| Revenue | | | | | |
| Gross Profit | | | | | |
| Gross Margin % | | | | | |
| Operating Income (EBIT) | | | | | |
| Operating Margin % | | | | | |
| EBITDA | | | | | |
| EBITDA Margin % | | | | | |
| Net Income | | | | | |
| Net Margin % | | | | | |
| EPS (Diluted) | | | | | |
| Shares Outstanding | | | | | |

**Revenue Breakdown by Segment (if available):**
| Segment | Revenue | % of Total | YoY Growth |
|---------|---------|------------|------------|
| | | | |

---

## Step 3: Balance Sheet Strength

| Metric | FY-2 | FY-1 | TTM | Change |
|--------|------|------|-----|--------|
| Cash & Equivalents | | | | |
| Total Current Assets | | | | |
| PP&E (Net) | | | | |
| Goodwill + Intangibles | | | | |
| Total Assets | | | | |
| Total Current Liabilities | | | | |
| Short-Term Debt | | | | |
| Long-Term Debt | | | | |
| Total Liabilities | | | | |
| Total Equity | | | | |
| Net Debt | | | | |

**Leverage Ratios:**
- Debt/EBITDA: __ (industry avg: __)
- Debt/Equity: __
- Interest Coverage: __x
- Current Ratio: __

---

## Step 4: Cash Flow Analysis

| Metric | FY-2 | FY-1 | TTM |
|--------|------|------|-----|
| Operating Cash Flow | | | |
| Capital Expenditures | | | |
| Free Cash Flow | | | |
| FCF Margin % | | | |
| FCF / Net Income (quality) | | | |
| Share Buybacks | | | |
| Dividends Paid | | | |
| Shareholder Yield % | | | |

---

## Step 5: Valuation Multiples

| Multiple | Current | 5Y Avg | Sector Median | Premium/Discount |
|----------|---------|--------|---------------|-----------------|
| P/E (TTM) | | | | |
| P/E (Fwd) | | | | |
| PEG Ratio | | | | |
| EV/EBITDA | | | | |
| EV/Revenue | | | | |
| P/FCF | | | | |
| P/B | | | | |
| P/S | | | | |
| FCF Yield % | | | | |
| Earnings Yield % | | | | |
| Dividend Yield % | | | | |

**Valuation Summary:**
- Trading at a [premium/discount/inline] to peers on [most metrics]
- [Most attractive multiple]: [value] vs [peer avg]
- [Most stretched multiple]: [value] vs [peer avg]

---

## Step 6: Growth Analysis

| Metric | 1Y | 3Y CAGR | 5Y CAGR | Projected (Analyst) |
|--------|-----|---------|---------|---------------------|
| Revenue Growth | | | | |
| EPS Growth | | | | |
| EBITDA Growth | | | | |
| FCF Growth | | | | |
| Dividend Growth | | | | |

**Growth Quality Assessment:**
- Organic vs acquisition-driven growth: ____
- Revenue predictability (subscription %): ____
- Pricing power evidence: ____

---

## Step 7: Profitability vs Peers

| Metric | [TICKER] | Peer 1 | Peer 2 | Peer 3 | Best-in-Class |
|--------|----------|--------|--------|--------|---------------|
| Gross Margin | | | | | |
| Operating Margin | | | | | |
| Net Margin | | | | | |
| ROE | | | | | |
| ROIC | | | | | |
| FCF Margin | | | | | |
| Revenue Growth | | | | | |
| EV/EBITDA | | | | | |

---

## Step 8: Economic Moat Assessment

Rate the width of the competitive moat (Wide / Narrow / None):

| Moat Source | Present? | Strength | Evidence |
|-------------|---------|---------|---------|
| Brand / Pricing Power | Yes / No | Strong / Moderate / Weak | |
| Network Effects | Yes / No | Strong / Moderate / Weak | |
| Switching Costs | Yes / No | Strong / Moderate / Weak | |
| Cost Advantages (scale) | Yes / No | Strong / Moderate / Weak | |
| Intangible Assets (IP, patents) | Yes / No | Strong / Moderate / Weak | |
| Regulatory / License Barriers | Yes / No | Strong / Moderate / Weak | |

**Overall Moat: Wide / Narrow / None**
Rationale: ____

---

## Step 9: Fundamental Score Dashboard

```
FUNDAMENTAL QUALITY SCORE — [TICKER]
════════════════════════════════════
Profitability:    __/25  — [commentary]
Valuation:        __/25  — [commentary]
Growth:           __/25  — [commentary]
Balance Sheet:    __/25  — [commentary]
────────────────────────────────────
Fundamental Score: __/100  Grade: [A+/A/B/C/D/F]

Key Strengths:
  ✓ [strength 1]
  ✓ [strength 2]
  ✓ [strength 3]

Key Concerns:
  ✗ [concern 1]
  ✗ [concern 2]
  ✗ [concern 3]
```

---

⚠️ Fundamental analysis is based on reported financials and public data. For educational purposes only. Not investment advice.
