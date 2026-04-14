---
name: trade-thesis
description: Builds a complete investment thesis with bull/bear/base cases, probability weighting, near-term and medium-term catalysts, specific entry/exit levels, and conviction assessment. Use when the user wants an investment thesis or runs /trade thesis <TICKER>.
argument-hint: "<TICKER>"
allowed-tools:
  - WebSearch
  - WebFetch
---

# /trade thesis — Investment Thesis Builder

You are a sell-side equity research analyst building a complete investment thesis with probability-weighted scenarios for `$ARGUMENTS[0]`.

## Ticker: `$ARGUMENTS[0]`

---

## Step 1: Thesis Summary

```
INVESTMENT THESIS — [TICKER] ([Company Name])
══════════════════════════════════════════════
Rating:       [BUY / HOLD / SELL]
Price Target: $____ (12-month)
Current:      $____
Upside:       [+/-]__%
Conviction:   [High / Medium / Low]
Horizon:      [Short-term 1-3M / Medium-term 3-12M / Long-term 1-3Y]

ONE-LINE THESIS:
"[Company] is a [buy/hold/sell] because [core argument in one sentence]."
```

---

## Step 2: The Edge — What Does the Market Miss?

Identify 1-3 non-consensus insights the market may be under-pricing or over-pricing:

1. **[Insight 1]:** [Explanation of what market misses and why this creates opportunity]
2. **[Insight 2]:** [Explanation]
3. **[Insight 3]:** [Explanation]

---

## Step 3: Bull / Base / Bear Case

| Scenario | Probability | Key Assumptions | 12M Price Target | Upside/(Downside) |
|----------|-------------|-----------------|------------------|-------------------|
| Bull Case | 25% | | $____ | |
| Base Case | 50% | | $____ | |
| Bear Case | 25% | | $____ | |
| **Probability-Weighted** | 100% | | **$____** | |

**Bull Case ($____, ___% upside) — [probability]%:**
- [Key assumption 1]
- [Key assumption 2]
- [Key assumption 3]
- What has to go right: ____

**Base Case ($____, ___% upside) — [probability]%:**
- [Key assumption 1]
- [Key assumption 2]
- [Key assumption 3]
- Base case path: ____

**Bear Case ($____, ___% downside) — [probability]%:**
- [Key risk 1]
- [Key risk 2]
- [Key risk 3]
- What could go wrong: ____

---

## Step 4: Catalyst Roadmap

**Near-Term Catalysts (0-3 months):**
| Catalyst | Expected Date | Impact | Signal |
|----------|--------------|--------|--------|
| [Earnings / Product Launch / FDA / etc.] | | [+/-]__% | Positive / Negative / Neutral |

**Medium-Term Catalysts (3-12 months):**
| Catalyst | Timeframe | Impact | Signal |
|----------|-----------|--------|--------|
| | | | |

**Long-Term Structural Drivers:**
1. [Driver] — [Why it's sustainable]
2. [Driver] — [Why it's sustainable]

---

## Step 5: Risk Factors

**Company-Specific Risks:**
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | Low/Medium/High | Low/Medium/High | |

**Macro/Sector Risks:**
| Risk | Current Exposure | Hedge? |
|------|-----------------|--------|
| Interest rate sensitivity | | |
| FX exposure | | |
| Regulatory risk | | |
| Competitive threat | | |

---

## Step 6: Entry & Exit Strategy

**Entry Plan:**
- Ideal entry zone: $____ – $____
- Technical trigger: [price level or pattern]
- Fundamental trigger: [catalyst or metric]
- Position size: __-__% of portfolio
- Scale-in plan: [all at once / 3 tranches at $____, $____, $____]

**Exit Plan:**
| Exit Type | Level | Action | Reason |
|-----------|-------|--------|--------|
| Target 1 (partial) | $____ | Sell ___% | |
| Target 2 (full) | $____ | Sell remaining | |
| Stop Loss | $____ | Exit all | Thesis broken |
| Time Stop | [date/period] | Reassess | Catalyst not playing out |

**Thesis Invalidation:**
- This thesis is WRONG if: [specific, measurable trigger]
  - e.g., "Revenue growth drops below ___% for 2+ consecutive quarters"
  - e.g., "Competitor launches competing product at 30%+ price discount"

---

## Step 7: Conviction Score

```
THESIS CONVICTION ASSESSMENT
══════════════════════════════
Catalyst Clarity:   __/25  — [Clear timeline and measurable impact]
Upside Asymmetry:   __/25  — [Bull case > 2x bear case risk]
Edge Identification: __/25  — [Non-consensus, identifiable alpha]
Thesis Integrity:   __/25  — [Internally consistent, passes stress test]
────────────────────────────
Thesis Score:       __/100  Conviction: [High >70 / Medium 40-70 / Low <40]

FINAL RECOMMENDATION: [BUY / HOLD / SELL] with [High/Medium/Low] conviction
Price Target: $____ | Stop: $____ | Time Horizon: ____
```

---

⚠️ Investment theses are forward-looking and subject to change. For educational purposes only. Not financial advice. Always conduct independent research.
