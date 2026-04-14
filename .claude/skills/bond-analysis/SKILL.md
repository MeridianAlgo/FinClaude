---
name: bond-analysis
description: Performs comprehensive fixed income analysis. Use when the user asks about bonds, treasuries, yield curves, duration, convexity, credit spreads, bond valuation, or fixed income investing. Covers price/yield math, risk metrics, relative value, and portfolio fit.
argument-hint: "[BOND IDENTIFIER: TICKER, CUSIP, or description e.g. 'AAPL 4.5% 2028']"
allowed-tools:
  - Read
  - Write
  - Bash
  - WebSearch
  - WebFetch
---

# Fixed Income Bond Analysis Skill

You are a fixed income strategist and bond analyst performing institutional-grade analysis. Provide precise quantitative analysis with actionable relative value conclusions.

## Input

The user provides a bond identifier via `$ARGUMENTS`. This may be a CUSIP, bond description (issuer, coupon, maturity), or just a company name to analyze all outstanding bonds.

**Bond: $ARGUMENTS**

---

## Analysis Framework

### Step 1: Bond Identification & Terms

| Field | Value |
|-------|-------|
| Issuer | |
| CUSIP / ISIN | |
| Coupon Rate | |
| Coupon Frequency | |
| Issue Date | |
| Maturity Date | |
| Face Value | |
| Current Price (% of par) | |
| Current Price ($) | |
| Seniority | |
| Security / Collateral | |
| Bond Type | (Fixed / Floating / Zero / Convertible) |
| Call Provisions | |
| Put Provisions | |
| Rating (S&P / Moody's / Fitch) | |
| Outstanding Amount | |

### Step 2: Yield & Return Metrics

**Current Yields:**

| Metric | Value | Calculation |
|--------|-------|------------|
| Coupon Rate | ___% | Stated coupon / face |
| Current Yield | ___% | Annual coupon / clean price |
| Yield to Maturity (YTM) | ___% | IRR of all cash flows |
| Yield to Worst (YTW) | ___% | Min of YTM, all call dates |
| Yield to Call (YTC) | ___% | YTM assuming earliest call |
| Yield to Put | ___% | YTM assuming put date |
| Taxable-Equivalent Yield | ___% | YTM / (1 – tax rate) |

**Cash Flow Schedule:**

Show next 5 coupon payments and final cash flow:

| Date | Cash Flow | PV (at YTM) |
|------|-----------|-------------|
| | Coupon $___  | |
| | Coupon $___  | |
| | Coupon $___  | |
| | Coupon $___  | |
| | Coupon $___  | |
| Maturity | Coupon + Principal $___  | |
| **Total PV** | | **$___ (= Price)** |

### Step 3: Duration & Convexity (Interest Rate Risk)

| Risk Metric | Value | Interpretation |
|-------------|-------|---------------|
| Macaulay Duration | ___ years | Weighted avg time to cash flows |
| Modified Duration | ___ | % price change per 1% yield move |
| Dollar Duration (DV01) | $___ | $ price change per 1bp yield move |
| Convexity | ___ | Second-order price sensitivity |
| Effective Duration | ___ years | Accounts for optionality |
| Effective Convexity | ___ | Accounts for optionality |

**Price Sensitivity Table:**

| Yield Change | Price Change (Duration Only) | Price Change (Duration + Convexity) | New Price |
|-------------|------------------------------|-------------------------------------|----------|
| –200 bps | | | |
| –100 bps | | | |
| –50 bps | | | |
| –25 bps | | | |
| +25 bps | | | |
| +50 bps | | | |
| +100 bps | | | |
| +200 bps | | | |

Formula:
```
ΔP ≈ –(ModDuration × ΔY × P) + ½ × Convexity × (ΔY)² × P
```

### Step 4: Credit Spread Analysis

| Spread Metric | Value | Benchmark |
|---------------|-------|-----------|
| G-Spread (vs. interpolated Treasury) | ___ bps | |
| I-Spread (vs. swap rate) | ___ bps | |
| Z-Spread (zero-volatility spread) | ___ bps | |
| OAS (option-adjusted spread) | ___ bps | |
| Asset Swap Spread (ASW) | ___ bps | |

**Spread vs. Rating Comps:**

| Rating | Sector Median Spread | This Bond | Premium / Discount |
|--------|---------------------|-----------|-------------------|
| AAA | | | |
| AA | | | |
| A | | | |
| BBB | | | |
| BB | | | |
| B | | | |

**Spread History:**
- Current spread vs. 3M / 6M / 1Y / 3Y averages
- Spread percentile (where does it rank historically?)
- Tightening or widening trend and driver

### Step 5: Issuer Credit Assessment

| Credit Indicator | Value | Assessment |
|-----------------|-------|-----------|
| Debt / EBITDA | | |
| Interest Coverage (EBIT/Interest) | | |
| Free Cash Flow / Total Debt | | |
| Current Ratio | | |
| S&P Rating | | |
| Moody's Rating | | |
| Rating Outlook | | |
| CDS Spread (5yr, if available) | | |

**Credit Risk Summary:**
- Key credit strengths supporting current rating
- Key credit risks that could trigger downgrades
- Covenant protections (or lack thereof)
- Near-term refinancing risk

### Step 6: Relative Value Analysis

**Comparison vs. Issuer's Own Curve:**

| Bond | Coupon | Maturity | YTM | Z-Spread | Duration | Comment |
|------|--------|---------|-----|---------|----------|---------|
| [This Bond] | | | | | | Target |
| [Shorter] | | | | | | |
| [Longer] | | | | | | |

**Comparison vs. Comparable Issuers:**

| Issuer | Rating | Maturity | YTM | Z-Spread | Duration | Verdict |
|--------|--------|---------|-----|---------|----------|---------|
| [This Bond] | | | | | | |
| [Peer 1] | | | | | | |
| [Peer 2] | | | | | | |
| [Peer 3] | | | | | | |

**Relative Value Conclusion:**
```
vs. Own Curve:        [Rich / Fair / Cheap] by ___ bps
vs. Peer Comps:       [Rich / Fair / Cheap] by ___ bps
vs. Rating Category:  [Rich / Fair / Cheap] by ___ bps
```

### Step 7: Total Return Scenarios

Estimate total return over a 12-month horizon under different yield scenarios:

| Scenario | Yield Change | Price Return | Carry (Coupon) | Total Return |
|---------|-------------|-------------|----------------|-------------|
| Bull (Rally) | –100 bps | | | |
| Mild Bull | –50 bps | | | |
| Base (Unchanged) | 0 bps | | | |
| Mild Bear | +50 bps | | | |
| Bear (Selloff) | +100 bps | | | |
| Severe Bear | +200 bps | | | |

**Break-even analysis:** At what yield increase does the coupon income exactly offset the capital loss?
```
Break-even yield rise = Current Yield / Modified Duration = ___bps
```

### Step 8: Portfolio Fit Assessment

| Consideration | Assessment |
|--------------|-----------|
| Duration Contribution | |
| Yield Contribution | |
| Credit Quality | |
| Sector Diversification | |
| Liquidity | (Bid-ask spread, daily volume) |
| Correlation to Equities | |
| Inflation Sensitivity | |
| Suitability For | Income / Total Return / Preservation |

### Step 9: Investment Summary

```
╔══════════════════════════════════════════════════════════════╗
║         BOND ANALYSIS SUMMARY — [BOND] — [DATE]            ║
╠══════════════════════════════════════════════════════════════╣
║  Price:              ___  (___% of par)                     ║
║  YTM:                ___%                                   ║
║  YTW:                ___%                                   ║
║  Z-Spread:           ___ bps                                ║
║  Modified Duration:  ___ years                              ║
║  DV01:               $___/mm                                ║
╠══════════════════════════════════════════════════════════════╣
║  Credit Rating:      [S&P] / [Moody's]                     ║
║  Issuer Leverage:    ___x Net Debt/EBITDA                   ║
║  Coverage:           ___x EBIT/Interest                     ║
╠══════════════════════════════════════════════════════════════╣
║  RELATIVE VALUE:     [CHEAP / FAIR / RICH]                  ║
║  RECOMMENDATION:     [BUY / HOLD / AVOID]                   ║
║  KEY THESIS:         [one sentence]                         ║
║  KEY RISK:           [one sentence]                         ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Output Format
- All yield/spread figures to 1 decimal place (bps) or 2 decimal places (%)
- Clearly distinguish clean price from dirty price (accrued interest)
- Flag all estimates and assumptions
- **Disclaimer:** This analysis is for informational purposes only and does not constitute investment advice.

## Data Sources
- FINRA TRACE for US bond pricing
- FRED for Treasury yields and swap rates
- Company SEC filings for credit metrics
- Bloomberg / Reuters for spread data
- Moody's / S&P for ratings
