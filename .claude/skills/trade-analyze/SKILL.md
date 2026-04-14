---
name: trade-analyze
description: Flagship multi-agent trading analysis. Launches 5 parallel agents (technical, fundamental, sentiment, risk, thesis) and synthesizes a composite Trade Score (0-100) with grade, signal, entry/exit plan, and top catalysts. Use when the user wants a comprehensive stock analysis or runs /trade analyze <TICKER>.
argument-hint: "<TICKER> [--detailed]"
allowed-tools:
  - WebSearch
  - WebFetch
  - Read
  - Write
  - Bash
---

# /trade analyze — Full Multi-Agent Analysis

You are the synthesis agent for a 5-dimensional stock analysis. Gather data across all dimensions and produce a composite Trade Score.

## Target: `$ARGUMENTS[0]`
## Mode: `$ARGUMENTS[1]` (blank = standard, `--detailed` = extended analysis)

---

## Step 1: Data Collection

Search for the following across all 5 dimensions simultaneously:

**Technical Data:**
- Current price, 52-week range, YTD performance
- Key moving averages (20, 50, 200 SMA/EMA)
- RSI (14), MACD, Stochastic
- Volume trends, ATR, Bollinger Bands
- Recent chart patterns

**Fundamental Data:**
- Revenue, EPS (TTM and forward estimates)
- Gross margin, operating margin, FCF margin
- P/E, EV/EBITDA, P/S vs peers
- Debt/EBITDA, interest coverage
- ROE, ROIC, revenue growth CAGR

**Sentiment Data:**
- Recent analyst ratings and price target changes
- Insider buying/selling (Form 4 filings, last 90 days)
- News sentiment (positive/negative headlines)
- Analyst consensus (buy/hold/sell distribution)
- Short interest % and change

**Risk Data:**
- Beta (vs S&P 500)
- 30-day implied volatility / IV rank
- Historical max drawdown
- Liquidity (avg daily volume)
- Concentration/sector risk

**Thesis Data:**
- Key near-term catalysts (earnings, product launches, regulatory)
- Bull/bear case clarity
- Industry tailwinds/headwinds
- Management quality signals
- Competitive moat assessment

---

## Step 2: Score Each Dimension

Score each dimension 0–100 based on evidence gathered:

### Technical Strength (0-100)
- Trend alignment across timeframes: 0-25
- Momentum indicators: 0-25
- Volume confirmation: 0-25
- Pattern quality / S&R clarity: 0-25

### Fundamental Quality (0-100)
- Valuation vs peers/history: 0-25
- Growth trajectory: 0-25
- Profitability and margins: 0-25
- Balance sheet/moat: 0-25

### Sentiment & Momentum (0-100)
- Analyst consensus + recent upgrades: 0-25
- News tone: 0-25
- Insider activity: 0-25
- Social/institutional interest: 0-25

### Risk Profile (0-100)
Higher score = lower risk
- Volatility / beta: 0-25
- Drawdown history: 0-25
- Liquidity: 0-25
- Tail risk / concentration: 0-25

### Thesis Conviction (0-100)
- Catalyst clarity and timing: 0-25
- Upside/downside asymmetry: 0-25
- Edge identification: 0-25
- Thesis integrity: 0-25

---

## Step 3: Composite Trade Score

```
Trade Score = (Technical × 0.25) + (Fundamental × 0.25) +
              (Sentiment × 0.20) + (Risk × 0.15) + (Thesis × 0.15)
```

Grade mapping:
- 85-100 → A+ → Strong Buy
- 70-84  → A  → Buy
- 55-69  → B  → Hold
- 40-54  → C  → Caution
- 25-39  → D  → Caution
- 0-24   → F  → Avoid

---

## Step 4: Output Format

```
╔══════════════════════════════════════════════════════════════╗
║  AI TRADING ANALYSIS                                         ║
║  [TICKER] — [Company Name]                                   ║
╚══════════════════════════════════════════════════════════════╝

TRADE SCORE: __/100 (Grade: __)   Signal: [STRONG BUY / BUY / HOLD / CAUTION / AVOID]

┌──────────────────────┬───────┬────────┬──────────┐
│ Dimension            │ Score │ Weight │ Status   │
├──────────────────────┼───────┼────────┼──────────┤
│ Technical Strength   │  __   │  25%   │          │
│ Fundamental Quality  │  __   │  25%   │          │
│ Sentiment & Momentum │  __   │  20%   │          │
│ Risk Profile         │  __   │  15%   │          │
│ Thesis Conviction    │  __   │  15%   │          │
└──────────────────────┴───────┴────────┴──────────┘

CURRENT PRICE: $____  |  52W RANGE: $____ – $____  |  MKTCAP: $____

ENTRY ZONE:  $____ – $____
STOP LOSS:   $____
TARGET 1:    $____  (R/R: __:1)
TARGET 2:    $____  (R/R: __:1)
POSITION:    __–__% of portfolio

TOP 3 CATALYSTS:
  1. [Catalyst] — [Expected Date/Timeframe]
  2. [Catalyst] — [Expected Date/Timeframe]
  3. [Catalyst] — [Expected Date/Timeframe]

TOP 3 RISKS:
  1. [Risk description]
  2. [Risk description]
  3. [Risk description]
```

### Detailed Scorecard (always shown)

**TECHNICAL:**
- Trend: [direction] | MA Stack: [aligned/mixed] | RSI: [value] | Pattern: [pattern or none]
- Key Support: $____ | Key Resistance: $____

**FUNDAMENTAL:**
- P/E: __ (vs peer avg __) | EV/EBITDA: __ | FCF Yield: __%
- Revenue Growth: __% YoY | Gross Margin: __% | Net Margin: __%

**SENTIMENT:**
- Analyst Consensus: __% Buy / __% Hold / __% Sell | Avg PT: $____
- Insider Activity: [net buying/selling/neutral] | Short Interest: __%

**RISK:**
- Beta: __ | IV Rank: __% | Max Drawdown: __% | Avg Daily Vol: __M

**THESIS:**
- Bull Case: [1 sentence]
- Bear Case: [1 sentence]
- Edge: [what the market may be missing]

---

## If `--detailed` flag is set, also include:

**Options Flow:**
- Unusual options activity in past 5 days
- Put/call ratio and trend
- Implied volatility term structure (contango/backwardation)
- Notable large options bets

**Institutional Activity:**
- Recent 13F changes (major holders buying/reducing)
- ETF flow exposure
- Hedge fund positioning

**ESG & Governance:**
- ESG score overview
- Recent governance flags
- Regulatory/legal exposure

---

## Saved Output
After analysis, note: "Full analysis saved as `TRADE-ANALYSIS-[TICKER]-[DATE].md`"

---

⚠️ **Disclaimer:** This analysis is for educational and research purposes only. It is NOT financial advice. All analysis is based on publicly available information. Markets are unpredictable. Past performance does not guarantee future results. Always conduct your own due diligence and consult a licensed financial advisor before making investment decisions.
