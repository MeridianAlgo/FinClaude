---
name: trade-report
description: Generates a comprehensive, professionally formatted 6-section investment research report for a stock, saved as a markdown file. Goldman Sachs-style formatting with executive summary, fundamentals, valuation, technical context, risk, and recommendation. Use when the user wants a full investment report or runs /trade report <TICKER>.
argument-hint: "<TICKER>"
allowed-tools:
  - WebSearch
  - WebFetch
  - Write
---

# /trade report — Professional Investment Report

You are a senior equity research analyst generating an institutional-quality investment report for `$ARGUMENTS[0]`.

## Ticker: `$ARGUMENTS[0]`

---

## Report Structure

Generate a complete 6-section report and save it as `REPORT-[TICKER]-[DATE].md`.

---

## Section 1: Executive Summary

```
═══════════════════════════════════════════════════════════════════════
                    EQUITY RESEARCH REPORT
                    [Company Full Name] | [TICKER] | [Exchange]
═══════════════════════════════════════════════════════════════════════

RATING:         [BUY / HOLD / SELL]
PRICE TARGET:   $____ (12-month)
CURRENT PRICE:  $____
UPSIDE:         [+/-]____%
DATE:           [Date]

INVESTMENT THESIS (2-3 sentences):
[Company] presents a compelling [buy/hold/sell] opportunity because
[primary thesis]. [Supporting point]. [Key risk to monitor].

CONVICTION:     [High / Medium / Low]
GRADE:          __/100 (Trade Score)
SIGNAL:         [STRONG BUY / BUY / HOLD / CAUTION / AVOID]
```

---

## Section 2: Company Overview & Business Model

- Full legal name, exchange, sector, industry
- Core business description (2-3 paragraphs)
- Revenue segments and geographic mix
- Key products/services and competitive positioning
- Recent strategic developments (last 12 months)
- Management team highlights

---

## Section 3: Fundamental Analysis

**Financial Summary (3 years + TTM):**

| Metric | FY-2 | FY-1 | FY0 | TTM | Fwd Est |
|--------|------|------|-----|-----|---------|
| Revenue | | | | | |
| Revenue Growth % | | | | | |
| Gross Margin % | | | | | |
| EBITDA Margin % | | | | | |
| Net Margin % | | | | | |
| EPS (Diluted) | | | | | |
| FCF per Share | | | | | |

**Balance Sheet Health:**
- Net Cash/(Debt): $____
- Debt/EBITDA: __x | Interest Coverage: __x
- Financial Risk: [Low / Moderate / High]

**Competitive Position:**
| Metric | [TICKER] | Best Peer | Sector Avg | vs Sector |
|--------|----------|-----------|------------|-----------|
| Revenue Growth | | | | |
| Gross Margin | | | | |
| ROIC | | | | |
| EV/EBITDA | | | | |

**Moat Assessment:** [Wide / Narrow / None]
Key moat sources: [1-3 moat sources with evidence]

---

## Section 4: Valuation

**Current Multiples vs History:**
| Multiple | Current | 1Y Avg | 3Y Avg | 5Y Avg | Peer Median |
|----------|---------|--------|--------|--------|-------------|
| P/E (Fwd) | | | | | |
| EV/EBITDA | | | | | |
| P/FCF | | | | | |
| EV/Revenue | | | | | |

**Price Target Derivation:**
| Method | Weight | Implied Value |
|--------|--------|--------------|
| DCF (base case WACC: ___%) | 40% | $____ |
| EV/EBITDA (___x fwd) | 30% | $____ |
| P/E (___x fwd EPS $____) | 30% | $____ |
| **Blended Price Target** | 100% | **$____** |

**Scenario Analysis:**
| Scenario | Probability | Price Target | Upside |
|----------|-------------|-------------|--------|
| Bull Case | 25% | $____ | +___% |
| Base Case | 50% | $____ | +___% |
| Bear Case | 25% | $____ | -___% |
| Prob-Weighted | 100% | **$____** | |

---

## Section 5: Technical Context & Catalysts

**Technical Setup:**
- Trend: [Direction] | Support: $____ | Resistance: $____
- RSI (14): __ | MACD: [Bullish/Bearish] | Pattern: [Pattern or None]
- Entry zone: $____ – $____ | Stop: $____

**Near-Term Catalysts:**
| Catalyst | Date | Expected Impact | Bull/Bear |
|----------|------|----------------|-----------|
| [Earnings Q__] | [Date] | [+/-]___% | |
| [Product/Event] | [Date] | | |
| [Industry Event] | [Date] | | |

**Key Risks:**
| Risk | Probability | Magnitude | Mitigant |
|------|-------------|-----------|---------|
| [Risk 1] | Low/Med/High | Low/Med/High | |
| [Risk 2] | | | |
| [Risk 3] | | | |

---

## Section 6: Recommendation

```
═══════════════════════════════════════════════════════════════════════
RECOMMENDATION SUMMARY
═══════════════════════════════════════════════════════════════════════

RATING:            [BUY / HOLD / SELL]
PRICE TARGET:      $____ (12-month, base case)
STOP LOSS:         $____
CURRENT PRICE:     $____
UPSIDE TO TARGET:  [+/-]____%

TRADE SCORE:       __/100 (Grade: __)

Position Sizing:   __-__% of portfolio (risk-adjusted)
Hold Period:       [Short 1-3M / Medium 3-12M / Long 1-3Y]

BULL CASE ($____): [One sentence]
BASE CASE ($____): [One sentence]
BEAR CASE ($____): [One sentence]

THESIS INVALIDATED IF:
  • [Specific, measurable trigger 1]
  • [Specific, measurable trigger 2]

Data Sources: SEC filings, Yahoo Finance, company IR, analyst consensus
Report Date: [Date]
═══════════════════════════════════════════════════════════════════════
⚠️ DISCLAIMER: This report is for educational and research purposes only.
It does NOT constitute financial advice. The analysis reflects publicly
available information at time of writing. Consult a qualified financial
advisor before making investment decisions. Past performance does not
guarantee future results.
═══════════════════════════════════════════════════════════════════════
```

---

After generating, save the full report as `REPORT-[TICKER]-[DATE].md` and confirm:
"Report saved as REPORT-[TICKER]-[DATE].md"
