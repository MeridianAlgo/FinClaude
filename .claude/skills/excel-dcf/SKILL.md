---
name: excel-dcf
description: Builds a complete DCF valuation model in Excel format (markdown tables). Produces Assumptions, FCF Projections, WACC calculation, Valuation, and Sensitivity Analysis sheets. Use when the user wants to build a DCF model or runs /excel-dcf <COMPANY>.
argument-hint: "<COMPANY_OR_TICKER> [optional: REVENUE GROWTH_RATE DISCOUNT_RATE]"
allowed-tools:
  - WebSearch
  - WebFetch
  - Write
---

# /excel-dcf — DCF Valuation Model Builder

You are a financial modeling specialist building an institutional-grade DCF model for `$ARGUMENTS[0]`. Structure the output as clearly delineated "sheets" in markdown format, designed to be copy-pasted into Excel.

## Company: `$ARGUMENTS[0]`
## Revenue Override (optional): `$ARGUMENTS[1]`
## Growth Rate Override (optional): `$ARGUMENTS[2]`
## Discount Rate Override (optional): `$ARGUMENTS[3]`

---

## SHEET 1: ASSUMPTIONS

```
DCF MODEL — [COMPANY NAME] ([TICKER])
Built: [Date]
Data Source: SEC Filings, Yahoo Finance, Company IR

═══════════════ HISTORICAL DATA ═══════════════

INCOME STATEMENT ($ millions)
                    FY-4    FY-3    FY-2    FY-1    FY0
Revenue           ___     ___     ___     ___     ___
Revenue Growth %  ___     ___     ___     ___     ___
Gross Profit      ___     ___     ___     ___     ___
Gross Margin %    ___     ___     ___     ___     ___
EBITDA            ___     ___     ___     ___     ___
EBITDA Margin %   ___     ___     ___     ___     ___
EBIT              ___     ___     ___     ___     ___
EBIT Margin %     ___     ___     ___     ___     ___
D&A               ___     ___     ___     ___     ___
Tax Rate %        ___     ___     ___     ___     ___
CapEx             ___     ___     ___     ___     ___
CapEx % Revenue   ___     ___     ___     ___     ___
Δ Working Capital ___     ___     ___     ___     ___
NWC % Revenue     ___     ___     ___     ___     ___

═══════════════ FORECAST ASSUMPTIONS ════════════

                    Y1      Y2      Y3      Y4      Y5
Revenue Growth %   ___     ___     ___     ___     ___
EBITDA Margin %    ___     ___     ___     ___     ___
D&A % Revenue      ___     ___     ___     ___     ___
CapEx % Revenue    ___     ___     ___     ___     ___
NWC % Revenue      ___     ___     ___     ___     ___
Tax Rate %         ___     ___     ___     ___     ___

Terminal Growth Rate: ___% (rationale: [reason])
WACC: ___% (derived below)
```

---

## SHEET 2: WACC CALCULATION

```
WACC COMPONENTS
═══════════════════════════════════════════════
Cost of Equity (CAPM):
  Risk-Free Rate (10Y Treasury):  ____%
  Beta (5Y monthly vs S&P 500):   ____
  Equity Risk Premium (Damodaran): ____%
  Size Premium:                   ____%
  Cost of Equity:                 ____%

Cost of Debt:
  Pre-Tax Cost of Debt:          ____%
  Tax Rate:                      ____%
  After-Tax Cost of Debt:        ____%

Capital Structure:
  Market Cap (Equity):           $___M (___% of EV)
  Total Debt:                    $___M (___% of EV)
  Enterprise Value:              $___M

WACC = (E/V × Ke) + (D/V × Kd × (1-T))
WACC = (___% × ___%) + (___% × ___%)
WACC = ____%
```

---

## SHEET 3: FCF PROJECTIONS

```
FREE CASH FLOW PROJECTIONS ($ millions)
═══════════════════════════════════════════════════════════════
                    Y1      Y2      Y3      Y4      Y5
Revenue            ___     ___     ___     ___     ___
Growth %           ___     ___     ___     ___     ___
EBITDA             ___     ___     ___     ___     ___
EBITDA Margin %    ___     ___     ___     ___     ___
(-)  D&A           ___     ___     ___     ___     ___
EBIT               ___     ___     ___     ___     ___
(-) Taxes          ___     ___     ___     ___     ___
NOPAT              ___     ___     ___     ___     ___
(+) D&A            ___     ___     ___     ___     ___
(-) CapEx          ___     ___     ___     ___     ___
(-) Δ NWC          ___     ___     ___     ___     ___
═══════════════════════════════════════════════════════════════
UNLEVERED FCF      ___     ___     ___     ___     ___
Discount Factor    ___     ___     ___     ___     ___
PV of FCF          ___     ___     ___     ___     ___
─────────────────────────────────────────────────────────────
Sum PV of FCFs:    $___M
```

---

## SHEET 4: VALUATION

```
TERMINAL VALUE
═══════════════════════════════════════════════════════════════
Gordon Growth Method:
  Final Year FCF:         $___M
  Terminal Growth Rate:    ____%
  WACC:                    ____%
  Terminal Value (TV):    $___M
  PV of Terminal Value:   $___M
  TV % of Total EV:        ____%   ← Should be <70%

Exit Multiple Method (cross-check):
  Final Year EBITDA:      $___M
  Exit Multiple:          ___x  (peer group: ___x)
  Terminal Value:         $___M
  PV of Terminal Value:   $___M

ENTERPRISE VALUE BRIDGE
═══════════════════════════════════════════════════════════════
(+) Sum PV of FCFs:       $___M
(+) PV of Terminal Value: $___M
   Enterprise Value:      $___M

(-) Total Debt:           $___M
(+) Cash & Equivalents:   $___M
(-) Minority Interest:    $___M
(-) Preferred Stock:      $___M
   Equity Value:          $___M

÷  Diluted Shares:        ___M
═══════════════════════════════════════════════════════════════
INTRINSIC VALUE:          $____
CURRENT PRICE:            $____
UPSIDE / (DOWNSIDE):      ____%
```

---

## SHEET 5: SENSITIVITY ANALYSIS

```
SENSITIVITY TABLE 1: Share Price vs WACC & Terminal Growth Rate
═══════════════════════════════════════════════════════════════
              g=1.5%   g=2.0%   g=2.5%   g=3.0%   g=3.5%
WACC-1.0%    $____    $____    $____    $____    $____
WACC-0.5%    $____    $____    $____    $____    $____
BASE WACC    $____    $____   [BASE]   $____    $____
WACC+0.5%    $____    $____    $____    $____    $____
WACC+1.0%    $____    $____    $____    $____    $____

SENSITIVITY TABLE 2: Share Price vs Revenue Growth & EBITDA Margin
═══════════════════════════════════════════════════════════════
              Mar-3%   Mar-2%   Mar-1%   BASE     Mar+1%
Gr-3%        $____    $____    $____    $____    $____
Gr-2%        $____    $____    $____    $____    $____
Gr-1%        $____    $____    $____    $____    $____
BASE         $____    $____    $____   [BASE]   $____
Gr+1%        $____    $____    $____    $____    $____

SCENARIO ANALYSIS
═══════════════════════════════════════════════════════════════
              Prob    Rev Growth   EBITDA%   WACC   Intrinsic
Bull Case     25%     ____%        ____%     ____%  $____
Base Case     50%     ____%        ____%     ____%  $____
Bear Case     25%     ____%        ____%     ____%  $____
───────────────────────────────────────────────────────────
PROBABILITY-WEIGHTED VALUE:                        $____
```

**SANITY CHECKS:**
- Terminal value as % of EV: ___% (target <70%)
- Implied exit multiple: ___x EBITDA
- Terminal ROIC: ___% vs WACC ___% (should be above WACC)
- Implied P/E: ___x (vs current ___x — reasonable?)

---

⚠️ This model is for educational and analytical purposes only. Assumptions drive all outputs — change assumptions carefully. Not investment advice.
