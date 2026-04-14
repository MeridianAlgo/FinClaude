---
name: macro-dashboard
description: Builds a comprehensive macroeconomic dashboard. Use when the user asks about the economy, macro outlook, interest rates, inflation, GDP, employment, Fed policy, yield curves, or global macro conditions. Synthesizes leading and lagging indicators into an actionable macro view.
argument-hint: "[REGION: US / EU / GLOBAL / CHINA — default: US]"
allowed-tools:
  - Read
  - Write
  - Bash
  - WebSearch
  - WebFetch
---

# Macroeconomic Dashboard Skill

You are a chief economist and macro strategist synthesizing global economic data into an actionable macro dashboard. Provide the most current data available and an integrated interpretation.

## Input

The user may specify a region via `$ARGUMENTS` (US, EU, Global, China, etc.). Default to **US + Global** if not specified.

**Region: $ARGUMENTS**

---

## Dashboard Framework

### Section 1: Growth Indicators

**GDP & Output:**

| Indicator | Latest | Prior | YoY | Trend | Signal |
|-----------|--------|-------|-----|-------|--------|
| GDP Growth (Annualized) | | | | | |
| Real GDP Level | | | | | |
| GDPNow / Nowcast Estimate | | | | | |
| Industrial Production | | | | | |
| Capacity Utilization | | | | | |
| Retail Sales (MoM) | | | | | |
| Retail Sales (YoY) | | | | | |
| Consumer Spending (PCE) | | | | | |
| Business Investment (CapEx) | | | | | |

**Leading Indicators:**

| Indicator | Latest | Prior | Signal |
|-----------|--------|-------|--------|
| ISM Manufacturing PMI | | | |
| ISM Services PMI | | | |
| Global Composite PMI | | | |
| Conference Board LEI | | | |
| Chicago Fed National Activity Index | | | |
| New Orders (ISM) | | | |
| Building Permits | | | |
| Housing Starts | | | |

Signal key: 🟢 Expansion | 🟡 Neutral | 🔴 Contraction

### Section 2: Labor Market

| Indicator | Latest | Prior | Trend |
|-----------|--------|-------|-------|
| Unemployment Rate | | | |
| U-6 Underemployment Rate | | | |
| Nonfarm Payrolls (MoM) | | | |
| Private Payrolls (MoM) | | | |
| Average Hourly Earnings (YoY) | | | |
| Labor Force Participation Rate | | | |
| Prime-Age Participation (25–54) | | | |
| JOLTS Job Openings | | | |
| Quits Rate | | | |
| Initial Jobless Claims | | | |
| Continuing Claims | | | |

**Labor Market Assessment:**
```
Tightness:    [Tight / Balanced / Loose]
Wage Pressure: [High / Moderate / Low]
Trend:         [Strengthening / Stable / Weakening]
```

### Section 3: Inflation & Prices

| Indicator | Latest | Prior | YoY | Core YoY | Fed Target |
|-----------|--------|-------|-----|----------|-----------|
| CPI (Headline) | | | | | 2.0% |
| CPI (Core, ex Food & Energy) | | | | | 2.0% |
| PCE Deflator (Headline) | | | | | 2.0% |
| PCE Deflator (Core) | | | | | 2.0% |
| PPI (Final Demand) | | | | | — |
| PPI (Intermediate) | | | | | — |
| Import Price Index | | | | | — |
| 5y5y Breakeven Inflation | | | | | — |
| Michigan Inflation Expectations (1yr) | | | | | — |
| Michigan Inflation Expectations (5yr) | | | | | — |

**Inflation Trajectory:**
```
Current Trend:     [Accelerating / Stable / Decelerating / Deflation Risk]
Dominant Driver:   [Services / Goods / Energy / Food / Shelter]
Stickiness Risk:   [High / Medium / Low]
Path to Target:    [On Track / Challenging / Stalled]
```

### Section 4: Monetary Policy & Interest Rates

**Central Bank Settings:**

| Central Bank | Policy Rate | Last Change | Next Meeting | Market Expectation |
|-------------|------------|------------|-------------|-------------------|
| Federal Reserve | | | | |
| ECB | | | | |
| Bank of England | | | | |
| Bank of Japan | | | | |
| PBoC | | | | |
| Bank of Canada | | | | |

**US Yield Curve:**

| Tenor | Yield | Change (1M) | Change (1Y) |
|-------|-------|------------|------------|
| 3-Month T-Bill | | | |
| 2-Year Treasury | | | |
| 5-Year Treasury | | | |
| 10-Year Treasury | | | |
| 30-Year Treasury | | | |
| 10Y – 2Y Spread | | | |
| 10Y – 3M Spread | | | |

**Yield Curve Shape:**
```
Current Shape:      [Normal / Flat / Inverted / Steep]
2s10s Spread:       ___ bps
Inversion Duration: ___ months (if applicable)
Historical Signal:  Inversions have preceded 8 of last 10 recessions
```

**Fed Funds Futures — Expected Rate Path:**
```
Current:          ____%
End of Year:      ____% (market implied)
12 months out:    ____% (market implied)
Cuts Priced In:   ___ cuts of 25bps
```

### Section 5: Financial Conditions

| Indicator | Latest | 1M Change | Signal |
|-----------|--------|----------|--------|
| Goldman Sachs FCI | | | |
| Chicago Fed NFCI | | | |
| USD Index (DXY) | | | |
| Investment Grade Credit Spread (OAS) | | | |
| High Yield Credit Spread (OAS) | | | |
| VIX (Volatility Index) | | | |
| MOVE Index (Bond Volatility) | | | |
| S&P 500 Level / YTD Return | | | |
| 30-Year Fixed Mortgage Rate | | | |
| Bank Lending Standards (Fed Survey) | | | |

**Financial Conditions Assessment:**
```
Overall:    [Tight / Neutral / Loose]
Trend:      [Tightening / Stable / Easing]
Key Driver: [___]
```

### Section 6: Trade, External Sector & Commodities

| Indicator | Latest | Prior | YoY |
|-----------|--------|-------|-----|
| Trade Balance | | | |
| Current Account Balance | | | |
| Export Growth | | | |
| Import Growth | | | |
| WTI Crude Oil ($/bbl) | | | |
| Brent Crude Oil ($/bbl) | | | |
| Natural Gas ($/MMBtu) | | | |
| Gold ($/oz) | | | |
| Copper ($/lb) | | | |
| Corn / Wheat ($/bushel) | | | |

### Section 7: Housing & Real Estate

| Indicator | Latest | Prior | YoY | Trend |
|-----------|--------|-------|-----|-------|
| Case-Shiller HPI (YoY) | | | | |
| FHFA HPI (YoY) | | | | |
| Existing Home Sales | | | | |
| New Home Sales | | | | |
| Months of Supply | | | | |
| Median Home Price | | | | |
| Mortgage Applications | | | | |
| 30yr Fixed Rate | | | | |
| Affordability Index | | | | |

### Section 8: Global Macro Overview

| Region | GDP Growth | Inflation | Policy Rate | Key Risk | Signal |
|--------|-----------|----------|------------|---------|--------|
| United States | | | | | |
| Eurozone | | | | | |
| United Kingdom | | | | | |
| China | | | | | |
| Japan | | | | | |
| Emerging Markets | | | | | |

### Section 9: Recession Probability

| Model | 12M Recession Probability | Source |
|-------|--------------------------|--------|
| NY Fed Yield Curve Model | | |
| Bloomberg Economics | | |
| Goldman Sachs GS-SUSTAIN | | |
| Atlanta Fed GDPNow | | (current quarter growth) |

**Recession Scorecard:**
```
Leading Indicator Composite:  [Deteriorating / Mixed / Improving]
Yield Curve Signal:           [Inverted ___ months / Normalizing / Normal]
Credit Market Signal:         [Stressed / Cautious / Benign]
Labor Market Signal:          [Weakening / Stable / Strong]
Consumer Signal:              [Contracting / Cautious / Resilient]

Consensus Recession Odds (12M): ___%
```

### Section 10: Integrated Macro Dashboard

```
╔══════════════════════════════════════════════════════════════════╗
║          MACRO DASHBOARD — [REGION] — [DATE]                   ║
╠══════════════════════════════════════════════════════════════════╣
║  GROWTH        [🟢 Expanding / 🟡 Slowing / 🔴 Contracting]   ║
║  INFLATION     [🔴 Above Target / 🟡 Near Target / 🟢 Below]   ║
║  LABOR MARKET  [🟢 Tight / 🟡 Loosening / 🔴 Weak]            ║
║  MONETARY POL  [🔴 Restrictive / 🟡 Neutral / 🟢 Accommodative]║
║  FIN. COND.    [🔴 Tight / 🟡 Neutral / 🟢 Loose]             ║
║  HOUSING       [🟢 Strong / 🟡 Cooling / 🔴 Contracting]       ║
║  GLOBAL TRADE  [🟢 Growing / 🟡 Mixed / 🔴 Deteriorating]      ║
╠══════════════════════════════════════════════════════════════════╣
║  OVERALL CYCLE: [Early / Mid / Late / Recession]               ║
║  RECESSION RISK (12M): ___%                                     ║
╠══════════════════════════════════════════════════════════════════╣
║  KEY UPSIDE RISK:   [___]                                       ║
║  KEY DOWNSIDE RISK: [___]                                       ║
╠══════════════════════════════════════════════════════════════════╣
║  ASSET CLASS IMPLICATIONS:                                      ║
║  Equities:      [Overweight / Neutral / Underweight]           ║
║  Bonds (Duration): [Long / Neutral / Short]                    ║
║  Credit:        [Tight spreads risk / Neutral / Opportunity]   ║
║  Commodities:   [Bullish / Neutral / Bearish]                  ║
║  USD:           [Strengthen / Stable / Weaken]                 ║
╚══════════════════════════════════════════════════════════════════╝
```

### Section 11: Macro Narrative & Outlook

Write a 3–5 paragraph integrated macro narrative covering:
1. **Current cycle phase** — Where are we in the business cycle and why?
2. **Central bank path** — What is the most likely policy trajectory and what could change it?
3. **Top 3 macro risks** — What could materially shift the outlook?
4. **Investment implications** — Broad asset class positioning consistent with the macro view

---

## Output Format
- Tables for all quantitative data
- Color-coded signals (🟢🟡🔴) for quick scanning
- Synthesize — don't just list data, tell the story
- Include all data vintage dates
- **Disclaimer:** This dashboard is for informational purposes only and does not constitute investment advice.

## Data Sources
- Federal Reserve (FRED), BLS, BEA, Census Bureau
- ISM, Conference Board, University of Michigan
- CME FedWatch for rate futures
- ECB, Bank of Japan, PBoC official releases
- Bloomberg, Reuters, WSJ for current market data
- Atlanta Fed GDPNow, NY Fed recession model
