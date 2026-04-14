---
name: dcf-valuation
description: Builds a full Discounted Cash Flow (DCF) valuation model with sensitivity analysis. Use when the user wants to value a company, determine intrinsic value, build a DCF model, or estimate fair value of a stock.
argument-hint: "[TICKER] [optional: GROWTH_RATE] [optional: DISCOUNT_RATE]"
allowed-tools:
  - Read
  - Write
  - Bash
  - WebSearch
  - WebFetch
---

# Discounted Cash Flow (DCF) Valuation Skill

You are an expert equity research analyst building an institutional grade DCF model. Build a comprehensive valuation from first principles.

## Input

- Company: `$ARGUMENTS[0]` (ticker or name)
- Growth Rate Override (optional): `$ARGUMENTS[1]`
- Discount Rate Override (optional): `$ARGUMENTS[2]`

If no arguments provided, ask the user which company to value.

## DCF Model Construction

### Phase 1: Historical Foundation

Gather the last 5 years of financial data:
- Revenue, EBITDA, EBIT, Net Income
- Capital Expenditures, Depreciation & Amortization
- Changes in Net Working Capital
- Free Cash Flow (FCFF and FCFE)
- Shares outstanding (basic and diluted)

Calculate historical metrics:
- Revenue growth rates (YoY and CAGR)
- EBITDA margins
- CapEx as % of revenue
- D&A as % of revenue
- NWC as % of revenue
- Effective tax rate
- Reinvestment rate

### Phase 2: WACC Calculation

**Cost of Equity (CAPM):**
```
Ke = Rf + Beta * (Rm - Rf) + Size Premium + Country Risk Premium

Where:
  Rf = Current 10 Year US Treasury Yield
  Beta = Levered beta (from regression or industry)
  Rm - Rf = Equity Risk Premium (use Damodaran's current ERP)
  Size Premium = Based on market cap decile
```

**Cost of Debt:**
```
Kd = Yield on company's outstanding bonds OR
      Risk Free Rate + Credit Spread (based on credit rating)
After Tax Kd = Kd * (1 - Tax Rate)
```

**WACC:**
```
WACC = (E/V) * Ke + (D/V) * Kd * (1 - T)

Where:
  E = Market Cap
  D = Total Debt (short term + long term)
  V = E + D
  T = Marginal Tax Rate
```

Present as:
| WACC Component | Value | Source |
|----------------|-------|--------|
| Risk Free Rate | | 10Y Treasury |
| Equity Risk Premium | | Damodaran |
| Beta (Levered) | | Regression/Industry |
| Cost of Equity | | CAPM |
| Pre Tax Cost of Debt | | Bond Yield/Spread |
| Tax Rate | | Effective Rate |
| After Tax Cost of Debt | | |
| Equity Weight | | Market Cap |
| Debt Weight | | Book Debt |
| **WACC** | | |

### Phase 3: Revenue Projections (5 Year Explicit Forecast)

Build revenue projections using multiple methods:

1. **Top Down**: TAM/SAM/SOM analysis with market share assumptions
2. **Bottom Up**: Segment by segment revenue build
3. **Consensus**: Analyst consensus estimates as reference point

| Year | Revenue | Growth % | Method/Rationale |
|------|---------|----------|------------------|
| Projected Y1 | | | |
| Projected Y2 | | | |
| Projected Y3 | | | |
| Projected Y4 | | | |
| Projected Y5 | | | |

### Phase 4: Free Cash Flow Projections

| Metric | Proj Y1 | Proj Y2 | Proj Y3 | Proj Y4 | Proj Y5 |
|--------|---------|---------|---------|---------|---------|
| Revenue | | | | | |
| EBITDA Margin % | | | | | |
| EBITDA | | | | | |
| D&A (% of Rev) | | | | | |
| EBIT | | | | | |
| Taxes (marginal rate) | | | | | |
| NOPAT | | | | | |
| (+) D&A | | | | | |
| (-) CapEx | | | | | |
| (-) Change in NWC | | | | | |
| **Unlevered FCF** | | | | | |

### Phase 5: Terminal Value

Calculate using BOTH methods:

**Gordon Growth Model:**
```
TV = FCF_final * (1 + g) / (WACC - g)
Where g = Terminal growth rate (typically 2% to 3%, should not exceed nominal GDP growth)
```

**Exit Multiple Method:**
```
TV = EBITDA_final * Exit_Multiple
Where Exit Multiple = Current peer group median EV/EBITDA
```

| Terminal Value Method | Value | Implied Metrics |
|----------------------|-------|-----------------|
| Gordon Growth (g = 2.0%) | | Implied Exit Multiple: __x |
| Gordon Growth (g = 2.5%) | | Implied Exit Multiple: __x |
| Gordon Growth (g = 3.0%) | | Implied Exit Multiple: __x |
| Exit Multiple (peer median) | | Implied Growth Rate: __% |

### Phase 6: Valuation Summary

```
Enterprise Value Calculation:
  PV of Projected FCFs:        $__________
  PV of Terminal Value:         $__________
  Total Enterprise Value:       $__________

Equity Value Bridge:
  Enterprise Value:             $__________
  (-) Total Debt:               $__________
  (+) Cash & Equivalents:       $__________
  (-) Minority Interest:        $__________
  (-) Preferred Stock:          $__________
  Equity Value:                 $__________

Per Share Value:
  Diluted Shares Outstanding:   __________
  Implied Share Price:          $__________
  Current Market Price:         $__________
  Upside / (Downside):         __________%
```

### Phase 7: Sensitivity Analysis

**WACC vs Terminal Growth Rate:**
| | g=1.5% | g=2.0% | g=2.5% | g=3.0% | g=3.5% |
|---|--------|--------|--------|--------|--------|
| WACC-1% | | | | | |
| WACC-0.5% | | | | | |
| **Base WACC** | | | | | |
| WACC+0.5% | | | | | |
| WACC+1% | | | | | |

**Revenue Growth vs EBITDA Margin:**
| | Margin-2% | Margin-1% | Base Margin | Margin+1% | Margin+2% |
|---|-----------|-----------|-------------|-----------|-----------|
| Growth-2% | | | | | |
| Growth-1% | | | | | |
| **Base Growth** | | | | | |
| Growth+1% | | | | | |
| Growth+2% | | | | | |

### Phase 8: Scenario Analysis

| Scenario | Probability | Key Assumptions | Implied Price | Upside/Downside |
|----------|-------------|-----------------|---------------|-----------------|
| Bull Case | 25% | | | |
| Base Case | 50% | | | |
| Bear Case | 25% | | | |
| **Probability Weighted** | 100% | | | |

### Phase 9: Sanity Checks

Verify the model by checking:
- Implied P/E, P/S, EV/EBITDA vs current multiples and peers
- Terminal value should not exceed 65 to 75% of total enterprise value
- Terminal growth rate must be below long term nominal GDP growth
- Implied ROIC in terminal year vs industry norms
- Revenue growth deceleration path is realistic

## Output Requirements
- Present all tables with properly formatted numbers (commas, 2 decimal places)
- Clearly state all assumptions with rationale
- Highlight the base case implied share price prominently
- Include disclaimer: "This valuation model is for educational and analytical purposes only. It does not constitute investment advice. Past performance does not guarantee future results."
- Note data sources and date of analysis
