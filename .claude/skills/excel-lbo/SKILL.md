---
name: excel-lbo
description: Builds a complete Leveraged Buyout (LBO) model. Produces Transaction Summary, Sources & Uses, Operating Model, Debt Schedule, Returns Analysis, and Debt Covenants sheets. Use when the user wants to build an LBO model or analyze a PE acquisition.
argument-hint: "<COMPANY> <ENTRY_EBITDA_MILLIONS> <ENTRY_MULTIPLE> [optional: HOLD_YEARS EXIT_MULTIPLE]"
allowed-tools:
  - WebSearch
  - WebFetch
---

# /excel-lbo — LBO Model Builder

You are a private equity analyst building a comprehensive LBO model for `$ARGUMENTS[0]`.

## Company: `$ARGUMENTS[0]`
## Entry EBITDA ($M): `$ARGUMENTS[1]`
## Entry Multiple (EV/EBITDA): `$ARGUMENTS[2]`
## Hold Period (optional): `$ARGUMENTS[3]` (default: 5 years)
## Exit Multiple (optional): `$ARGUMENTS[4]` (default: same as entry)

---

## SHEET 1: TRANSACTION SUMMARY

```
LBO MODEL — [COMPANY NAME]
Sponsor: [PE Firm or Generic]
Date: [Date]

TRANSACTION OVERVIEW
═══════════════════════════════════════════════════════════════
Entry EBITDA:           $___M
Entry Multiple:         ___x EV/EBITDA
Enterprise Value:       $___M
  (+) Transaction Fees: $___M  (2% of EV)
  (+) Financing Fees:   $___M  (3% of debt)
Total Uses:             $___M

CAPITAL STRUCTURE
═══════════════════════════════════════════════════════════════
                    $M      % of Total   x EBITDA   Interest Rate
Senior Secured      ___     ____%        ___x       SOFR + ___% (___% total)
Senior Unsecured    ___     ____%        ___x       Fixed ____%
Mezzanine           ___     ____%        ___x       Fixed ____%
─────────────────────────────────────────────────────────────
Total Debt          ___     ____%        ___x
Sponsor Equity      ___     ____%
─────────────────────────────────────────────────────────────
Total Capital       ___     100.0%

KEY METRICS
  Total Leverage:    ___x EBITDA
  Senior Leverage:   ___x EBITDA
  Interest Coverage: ___x (EBITDA / Total Interest)
  Equity Check:      $___M (___% of EV)
```

---

## SHEET 2: SOURCES & USES

```
SOURCES & USES OF FUNDS ($M)
═══════════════════════════════════════════════════════════════
SOURCES                         USES
Senior Secured:    $___M        Purchase Price (EV):    $___M
Senior Unsecured:  $___M        Refinance Existing Debt:$___M
Mezzanine:         $___M        Transaction Fees:       $___M
Sponsor Equity:    $___M        Financing Fees:         $___M
Mgmt Rollover:     $___M        Working Capital:        $___M
─────────────────────────────────────────────────────────────
TOTAL SOURCES:     $___M        TOTAL USES:             $___M
```

---

## SHEET 3: OPERATING MODEL

```
OPERATING MODEL ($M)
═══════════════════════════════════════════════════════════════
                    Entry   Y1      Y2      Y3      Y4      Y5
Revenue             ___     ___     ___     ___     ___     ___
  Growth %                  ___     ___     ___     ___     ___
EBITDA              ___     ___     ___     ___     ___     ___
  EBITDA Margin %   ___     ___     ___     ___     ___     ___
  D&A               ___     ___     ___     ___     ___     ___
EBIT                ___     ___     ___     ___     ___     ___
  Interest Expense  ___     ___     ___     ___     ___     ___
EBT                 ___     ___     ___     ___     ___     ___
  Taxes             ___     ___     ___     ___     ___     ___
Net Income          ___     ___     ___     ___     ___     ___

CASH FLOW FOR DEBT SERVICE
  EBITDA             ___     ___     ___     ___     ___
  (-) Cash Interest  ___     ___     ___     ___     ___
  (-) CapEx          ___     ___     ___     ___     ___
  (-) Δ NWC          ___     ___     ___     ___     ___
  (-) Cash Taxes     ___     ___     ___     ___     ___
  = Free Cash Flow   ___     ___     ___     ___     ___
  (-) Mandatory Amort___     ___     ___     ___     ___
  = Cash for Sweep   ___     ___     ___     ___     ___
```

---

## SHEET 4: DEBT SCHEDULE

```
DEBT SCHEDULE ($M)
═══════════════════════════════════════════════════════════════
SENIOR SECURED TERM LOAN
                    Y1      Y2      Y3      Y4      Y5
Beginning Balance   ___     ___     ___     ___     ___
  (-) Amortization  ___     ___     ___     ___     ___
  (-) Cash Sweep    ___     ___     ___     ___     ___
Ending Balance      ___     ___     ___     ___     ___
Interest Expense    ___     ___     ___     ___     ___

SENIOR UNSECURED NOTES (PIK/Cash)
Beginning Balance   ___     ___     ___     ___     ___
  (+) PIK Interest  ___     ___     ___     ___     ___
  (-) Repayment     ___     ___     ___     ___     ___
Ending Balance      ___     ___     ___     ___     ___

TOTAL DEBT SUMMARY
Total Debt BOY      ___     ___     ___     ___     ___
Total Debt EOY      ___     ___     ___     ___     ___
Total Net Debt      ___     ___     ___     ___     ___
Leverage (x EBITDA) ___     ___     ___     ___     ___
Interest Coverage   ___     ___     ___     ___     ___
```

---

## SHEET 5: RETURNS ANALYSIS

```
EXIT ANALYSIS ($M)
═══════════════════════════════════════════════════════════════
Hold Period:        ___ years
Entry Date:         [Date]
Exit Date:          [Date]

Exit Multiple:      ___x (vs entry ___x)
Exit EBITDA:        $___M
Exit EV:            $___M

EQUITY BRIDGE:
Exit EV:            $___M
(-) Net Debt at Exit:$___M
(-) Management Fees: $___M
Exit Equity Value:  $___M

RETURNS
═══════════════════════════════════════════════════════════════
Initial Equity:     $___M
Exit Equity:        $___M
MOIC:               ___x   (target: 2.0x-3.5x for 5 years)
IRR:                ____%  (target: 20%+)

RETURNS SENSITIVITY — MOIC (x)
Exit Multiple →     6x      7x      8x      9x      10x
Rev Gr 5%          ___     ___     ___     ___     ___
Rev Gr 7%          ___     ___     ___     ___     ___
Rev Gr 9%  (BASE)  ___     ___    [___]   ___     ___
Rev Gr 11%         ___     ___     ___     ___     ___
Rev Gr 13%         ___     ___     ___     ___     ___

RETURNS SENSITIVITY — IRR (%)
Exit Multiple →     6x      7x      8x      9x      10x
Rev Gr 5%          ___     ___     ___     ___     ___
Rev Gr 7%          ___     ___     ___     ___     ___
Rev Gr 9%  (BASE)  ___     ___    [___]   ___     ___
Rev Gr 11%         ___     ___     ___     ___     ___
Rev Gr 13%         ___     ___     ___     ___     ___
```

---

## SHEET 6: DEBT COVENANTS

```
DEBT COVENANTS (MAINTENANCE)
═══════════════════════════════════════════════════════════════
Covenant             Test     Y1      Y2      Y3      Y4      Y5
Max Leverage         ___x     ___     ___     ___     ___     ___
  Headroom                    ___     ___     ___     ___     ___
Min Interest Coverage___x     ___     ___     ___     ___     ___
  Headroom                    ___     ___     ___     ___     ___
Max Capex            $___M    ___     ___     ___     ___     ___
Min Liquidity        $___M    ___     ___     ___     ___     ___
═══════════════════════════════════════════════════════════════
Status (all years):  PASS / WARNING / BREACH

COVENANT STRESS TEST (Downside -20% EBITDA):
Max Leverage:        ___x (limit ___x) → [PASS / BREACH]
Min Coverage:        ___x (limit ___x) → [PASS / BREACH]
```

---

⚠️ LBO models are highly sensitive to assumptions. Returns depend heavily on exit multiple and operational performance. For educational purposes only. Not investment advice.
