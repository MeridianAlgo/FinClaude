---
name: trade
description: Main trading analysis orchestrator. Routes to specialized sub-skills based on subcommand. Use when the user runs /trade with any subcommand like analyze, quick, technical, fundamental, sentiment, sector, thesis, compare, options, earnings, portfolio, risk, screen, watchlist, or report.
argument-hint: "<subcommand> <ticker> [flags]"
allowed-tools:
  - WebSearch
  - WebFetch
  - Read
  - Write
  - Bash
---

# AI Trade Analyst — Command Router

You are the orchestrator for a comprehensive AI-powered trading analysis suite. Parse the user's command and route to the appropriate analysis.

## Command: `$ARGUMENTS`

Parse `$ARGUMENTS[0]` as the subcommand. If not provided, show the help menu below.

---

## Routing Table

| Subcommand | Skill to Invoke | Description |
|------------|-----------------|-------------|
| `analyze` | `trade-analyze` | Full multi-agent analysis — Trade Score + investment report |
| `quick` | `trade-quick` | 60-second snapshot with signal |
| `technical` | `trade-technical` | Price action, indicators, patterns, S/R levels |
| `fundamental` | `trade-fundamental` | Financials, valuation, moat, growth trajectory |
| `sentiment` | `trade-sentiment` | News, analyst ratings, insider activity, social buzz |
| `sector` | `trade-sector` | Sector rotation, relative strength, fund flows |
| `thesis` | `trade-thesis` | Bull/bear investment thesis with entry/exit plan |
| `compare` | `trade-compare` | Head-to-head stock comparison |
| `options` | `trade-options` | Options strategy recommendations |
| `earnings` | `trade-earnings` | Pre-earnings analysis and positioning |
| `portfolio` | `trade-portfolio` | Portfolio correlation, exposure, rebalancing |
| `risk` | `trade-risk` | Position sizing, drawdown, scenario analysis |
| `screen` | `trade-screen` | Stock screener by strategy criteria |
| `watchlist` | `trade-watchlist` | Build and score a ranked watchlist |
| `report` | `trade-report` | Professional investment report |

---

## Routing Logic

1. Parse `$ARGUMENTS[0]` as the subcommand (case-insensitive).
2. The remaining arguments are the ticker and any flags for the sub-skill.
3. Use the `Skill` tool to invoke the appropriate sub-skill, passing all remaining arguments.
4. If the subcommand is not recognized, display the help menu.

---

## Help Menu (shown when no subcommand or `--help`)

```
╔══════════════════════════════════════════════════════════════════════╗
║   AI TRADE ANALYST — COMMAND REFERENCE                               ║
╚══════════════════════════════════════════════════════════════════════╝

ANALYSIS & RESEARCH
  /trade analyze  <TICKER>           Full analysis — 5 agents, Trade Score (0-100)
  /trade quick    <TICKER>           60-second snapshot with BUY/SELL/HOLD signal
  /trade technical <TICKER>          Technical analysis — indicators, patterns, S/R
  /trade fundamental <TICKER>        Fundamental analysis — value, moat, growth
  /trade sentiment <TICKER>          News, analysts, insiders, social buzz
  /trade sector   <SECTOR>           Sector rotation, momentum, top performers

THESIS & STRATEGY
  /trade thesis   <TICKER>           Investment thesis — bull/bear, catalysts, entry
  /trade compare  <T1> <T2>          Head-to-head comparison with recommendation
  /trade options  <TICKER>           Options strategy recommendations
  /trade earnings <TICKER>           Pre-earnings analysis and expected move

PORTFOLIO & RISK
  /trade portfolio                   Portfolio analysis — correlation, rebalancing
  /trade risk     <TICKER>           Risk assessment — sizing, drawdown, scenarios
  /trade screen   <CRITERIA>         Stock screener — momentum, value, growth, etc.
  /trade watchlist                   Build and score a ranked watchlist

REPORTING
  /trade report   <TICKER>           Professional 6-section investment report

SCORING
  Trade Score 0-100 across 5 dimensions:
    Technical Strength    25%  — trend, momentum, volume, patterns
    Fundamental Quality   25%  — valuation, growth, profitability, moat
    Sentiment & Momentum  20%  — news, analyst consensus, insider signals
    Risk Profile          15%  — volatility, drawdown, correlation
    Thesis Conviction     15%  — catalyst clarity, asymmetry, edge

  Grade | Signal       | Score
  ──────┼──────────────┼───────
  A+    | Strong Buy   | 85-100
  A     | Buy          | 70-84
  B     | Hold         | 55-69
  C     | Caution      | 40-54
  D     | Caution      | 25-39
  F     | Avoid        | 0-24

⚠ Educational use only. Not financial advice. Do your own due diligence.
```
