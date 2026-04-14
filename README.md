# FinClaude

### Institutional Grade Financial Analysis Skills for Claude Code

> 35 AI powered skills, 8 Python computation tools, and a 5 agent trading analysis system, all driven by natural language. No API keys. No brokerage accounts. No financial data subscriptions. Just Claude Code.

**License:** MIT | **Status:** Active | **Skills:** 35 | **Python Tools:** 8 | **Agents:** 5

---

> **Disclaimer:** This toolkit is for educational and research purposes only. It is NOT financial advice. It does NOT execute trades, manage portfolios, or connect to any brokerage. All analysis is based on publicly available information. Always do your own due diligence and consult a licensed financial advisor before making investment decisions.

---

## What Is This

FinClaude is a comprehensive collection of Claude Code skills that transform Claude into a professional grade financial analyst. Each skill is a self contained prompt framework that instructs Claude to perform rigorous, multi step analysis across every major domain of finance, from equity research and options pricing to macroeconomic dashboards and M&A deal evaluation.

Every skill outputs structured, institutional quality analysis with formatted tables, dashboards, sensitivity matrices, and clear verdicts.

## Key Capabilities

| Domain | What You Get |
|--------|-------------|
| Equity Research | Full company analysis, financial statements, competitive positioning, bull/bear scenarios |
| DCF Valuation | 9 phase DCF model with WACC, sensitivity tables, scenario analysis, and sanity checks |
| Options Pricing | Black Scholes and binomial pricing, all Greeks, strategy payoff diagrams, IV analysis |
| Technical Analysis | 20+ indicators, support/resistance levels, chart patterns, fibonacci, pivot points |
| Portfolio Optimization | Mean variance optimization, efficient frontier, Monte Carlo simulation, stress testing |
| Risk Assessment | Parametric, historical, and Monte Carlo VaR, CVaR, tail risk, factor decomposition |
| Credit Analysis | Altman Z Score, Merton model, covenant analysis, capital structure waterfall |
| Bond Analysis | Yield/duration/convexity, credit spreads, relative value, total return scenarios |
| Earnings Analysis | Estimates vs actuals, beat/miss history, guidance tracking, call sentiment |
| Macro Dashboard | GDP, inflation, labor, Fed policy, yield curves, recession probability |
| Dividend Analysis | Safety scoring, payout coverage, DDM valuation, growth projections |
| IPO Analysis | S 1 prospectus review, valuation vs comps, lockup risk, participation verdict |
| M&A Analysis | Synergies, accretion/dilution, deal structure, regulatory risk, LBO feasibility |
| Financial Reporting | Goldman Sachs style initiation reports with football field valuation |
| Ratio Analysis | 60+ ratios with peer benchmarking and DuPont decomposition |
| Excel Modeling | DCF and LBO models formatted as structured sheets for Excel export |
| Trading Analysis | 5 agent system with composite Trade Score (0 to 100), entry/exit plans |
| Sector Analysis | Rotation trends, relative strength, fund flows, top performers |

---

## Quick Start

### Prerequisites

- Claude Code CLI (version 2.0.11 or higher)
- Claude paid subscription (Pro, Team, or Enterprise)
- Internet connection for real time data retrieval

### Installation

Clone the repository and start using the skills immediately:

```bash
git clone https://github.com/MeridianAlgo/FinClaude.git
cd FinClaude
```

Open the project in Claude Code and the skills will be automatically available.

### Usage

Simply ask Claude to perform an analysis in natural language, or invoke a specific skill:

```
Analyze Apple's financials
```

```
Build a DCF model for NVDA
```

```
Price a call option for TSLA with strike 250 expiring in 30 days
```

```
/trade analyze AAPL
```

```
Run a macro dashboard for the US economy
```

---

## All Skills

### Fundamental Analysis (14 Skills)

| Skill | Command / Trigger | Description |
|-------|------------------|-------------|
| Financial Analysis | Analyze [TICKER] | Deep fundamental analysis with income statement, balance sheet, and cash flow tables |
| DCF Valuation | Value [TICKER] / Build a DCF for [TICKER] | 9 phase DCF model with WACC calculation and sensitivity analysis |
| Ratio Analysis | Financial ratios for [TICKER] | 60+ ratios across profitability, liquidity, solvency, efficiency, and valuation |
| Earnings Analyzer | Analyze earnings for [TICKER] | Estimates vs actuals, guidance tracking, call sentiment, quality of earnings |
| Credit Analysis | Credit analysis for [TICKER] | Altman Z Score, Merton model, covenant analysis, capital structure waterfall |
| Bond Analysis | Analyze [BOND] | Yield, duration, convexity, credit spreads, relative value, total return scenarios |
| Dividend Analysis | Dividend analysis for [TICKER] | Safety score (out of 40), payout coverage, DDM valuation, growth projections |
| IPO Analysis | Analyze the [COMPANY] IPO | S 1 review, valuation vs comps, lockup risk, IPO scorecard, participation verdict |
| M&A Analysis | Analyze [ACQUIRER] acquiring [TARGET] | Synergies, accretion/dilution, deal financing, regulatory risk, LBO feasibility |
| Financial Report | Write a research report on [TICKER] | Goldman Sachs style initiation report with 10 sections and football field valuation |
| Macro Dashboard | Show me the macro dashboard | 11 section economic dashboard with growth, inflation, labor, policy, and recession odds |
| Portfolio Optimizer | Optimize portfolio [TICKERS] | Mean variance optimization, efficient frontier, Monte Carlo, stress testing |
| Risk Assessment | Risk assessment for [TICKER] | Three method VaR, CVaR, drawdown analysis, stress testing, factor decomposition |
| Options Pricer | Price a [CALL/PUT] for [TICKER] | Black Scholes and binomial pricing, all Greeks, IV analysis, strategy payoffs |

### Technical Analysis (1 Skill)

| Skill | Command / Trigger | Description |
|-------|------------------|-------------|
| Technical Analysis | Technical analysis for [TICKER] | 20+ indicators, multi timeframe trends, chart patterns, support/resistance, signals |

### Excel Modeling (2 Skills)

| Skill | Command / Trigger | Description |
|-------|------------------|-------------|
| Excel DCF | Build an Excel DCF for [COMPANY] | 5 sheet DCF model with assumptions, WACC, FCF projections, valuation, sensitivity |
| Excel LBO | Build an LBO model for [COMPANY] | 6 sheet LBO with transaction summary, sources and uses, operating model, debt schedule, returns |

### AI Trading Analyst (16 Skills)

The trading analysis suite uses a command router (`/trade`) that dispatches to 15 specialized sub skills:

| Command | Description |
|---------|-------------|
| `/trade analyze [TICKER]` | Flagship 5 agent analysis with composite Trade Score (0 to 100) |
| `/trade quick [TICKER]` | 60 second snapshot with BUY/SELL/HOLD signal |
| `/trade technical [TICKER]` | Technical analysis with indicators, patterns, and support/resistance |
| `/trade fundamental [TICKER]` | Fundamental analysis with valuation, moat, and growth trajectory |
| `/trade sentiment [TICKER]` | News, analyst ratings, insider activity, and social sentiment |
| `/trade sector [SECTOR]` | Sector rotation, relative strength, and fund flows |
| `/trade thesis [TICKER]` | Bull/bear investment thesis with entry/exit plan |
| `/trade compare [T1] [T2]` | Head to head stock comparison with recommendation |
| `/trade options [TICKER]` | Options strategy recommendations based on outlook |
| `/trade earnings [TICKER]` | Pre earnings analysis with expected move and positioning |
| `/trade portfolio` | Portfolio correlation, sector exposure, and rebalancing |
| `/trade risk [TICKER]` | Position sizing, max drawdown, and scenario analysis |
| `/trade screen [CRITERIA]` | Stock screener by strategy (momentum, value, dividend, growth) |
| `/trade watchlist` | Build and score a ranked watchlist |
| `/trade report [TICKER]` | Professional 6 section investment report |

### Other Skills (2 Skills)

| Skill | Description |
|-------|-------------|
| Trading Ideas | Comprehensive equity research with BUY/SELL/HOLD recommendation |
| Queue | Task queue processor for chaining analyses |

---

## Trade Score Methodology

The flagship `/trade analyze` command scores stocks across 5 dimensions with a weighted composite:

| Category | Weight | What It Measures |
|----------|--------|-----------------|
| Technical Strength | 25% | Trend, momentum, volume, pattern quality, support/resistance |
| Fundamental Quality | 25% | Valuation, growth, profitability, balance sheet, moat |
| Sentiment and Momentum | 20% | News tone, social buzz, analyst consensus, insider signals |
| Risk Profile | 15% | Volatility, drawdown potential, correlation, liquidity |
| Thesis Conviction | 15% | Catalyst clarity, timeline, asymmetry, edge identification |

### Grade and Signal Mapping

| Score | Grade | Signal |
|-------|-------|--------|
| 85 to 100 | A+ | Strong Buy |
| 70 to 84 | A | Buy |
| 55 to 69 | B | Hold |
| 40 to 54 | C | Caution |
| 25 to 39 | D | Caution |
| 0 to 24 | F | Avoid |

---

## Sample Output

### /trade analyze AAPL

```
╔══════════════════════════════════════════════════════════════╗
║  AI TRADING ANALYSIS                                         ║
║  AAPL — Apple Inc.                                           ║
╚══════════════════════════════════════════════════════════════╝

TRADE SCORE: 74/100 (Grade: A)  Signal: BUY

┌──────────────────────┬───────┬────────┬──────────┐
│ Category             │ Score │ Weight │ Status   │
├──────────────────────┼───────┼────────┼──────────┤
│ Technical Strength   │ 78    │ 25%    │ Strong   │
│ Fundamental Quality  │ 82    │ 25%    │ Strong   │
│ Sentiment & Momentum │ 68    │ 20%    │ Mixed    │
│ Risk Profile         │ 62    │ 15%    │ Mixed    │
│ Thesis Conviction    │ 71    │ 15%    │ Strong   │
└──────────────────────┴───────┴────────┴──────────┘

ENTRY: $178-$182  |  TARGET: $198-$205  |  STOP: $168
RISK/REWARD: 2.8:1  |  POSITION: 3-5% of portfolio

TOP 3 CATALYSTS:
  1. Q3 earnings (Jul 31) — services growth + AI roadmap
  2. iPhone 17 launch (Sep) — AI features as upgrade driver
  3. Margin expansion from services mix shift
```

---

## Python Computation Tools

The `.claude/tools/` directory contains 8 Python scripts that Claude can invoke for precise numerical computation:

| Tool | Description |
|------|-------------|
| `black_scholes.py` | Black Scholes Merton options pricing with all Greeks |
| `bond.py` | Fixed income yield, duration, convexity, and price calculations |
| `dcf.py` | DCF model computation with WACC and terminal value |
| `portfolio.py` | Portfolio optimization, correlation matrices, and efficient frontier |
| `ratios.py` | Financial ratio computation engine (60+ ratios) |
| `technicals.py` | Technical indicator calculations (RSI, MACD, Bollinger, etc.) |
| `zscore.py` | Altman Z Score and credit scoring calculations |
| `inbox.py` | Task queue management for chaining multiple analyses |

---

## Architecture

```
                         User Request
                              |
                    ┌─────────┼─────────┐
                    |         |         |
             ┌──────┴───┐ ┌──┴───┐ ┌───┴──────┐
             | Skill     | | Tool | | Trading  |
             | Framework | | Engine| | Agents   |
             | (35 SKILL | | (8 Py| | (5 agent |
             |  .md)     | | tools)| | system)  |
             └──────────┘ └──────┘ └──────────┘
                    |         |         |
                    └─────────┼─────────┘
                              |
                    ┌─────────┴─────────┐
                    |   Claude Code AI  |
                    |   Web Search +    |
                    |   Computation     |
                    └───────────────────┘
                              |
                    ┌─────────┴─────────┐
                    |  Structured Output |
                    |  Tables, Dashboards|
                    |  Scores, Verdicts  |
                    └───────────────────┘
```

---

## Project Structure

```
FinClaude/
├── README.md                              # This file
├── CLAUDE.md                              # Project conventions and skill index
├── Synthesis.md                           # Reference documentation
├── INBOX.md                               # Task queue for chaining analyses
├── .claude/
│   ├── settings.local.json                # Claude Code local settings
│   ├── skills/                            # All 35 analysis skills
│   │   ├── financial-analysis/SKILL.md    # Deep fundamental analysis
│   │   ├── dcf-valuation/SKILL.md         # DCF modeling
│   │   ├── ratio-analysis/SKILL.md        # Financial ratio computation
│   │   ├── portfolio-optimizer/SKILL.md   # MPT portfolio optimization
│   │   ├── options-pricer/SKILL.md        # Options pricing and Greeks
│   │   ├── technical-analysis/SKILL.md    # Chart patterns and indicators
│   │   ├── risk-assessment/SKILL.md       # VaR and stress testing
│   │   ├── earnings-analyzer/SKILL.md     # Earnings analysis
│   │   ├── credit-analysis/SKILL.md       # Credit risk scoring
│   │   ├── macro-dashboard/SKILL.md       # Macroeconomic dashboard
│   │   ├── financial-report/SKILL.md      # Sell side research reports
│   │   ├── bond-analysis/SKILL.md         # Fixed income analysis
│   │   ├── dividend-analysis/SKILL.md     # Dividend sustainability
│   │   ├── ipo-analysis/SKILL.md          # IPO prospectus analysis
│   │   ├── m-and-a-analysis/SKILL.md      # M&A deal analysis
│   │   ├── excel-dcf/SKILL.md             # Excel format DCF model
│   │   ├── excel-lbo/SKILL.md             # Excel format LBO model
│   │   ├── trade/SKILL.md                 # Trade command router
│   │   ├── trade-analyze/SKILL.md         # 5 agent full analysis
│   │   ├── trade-quick/SKILL.md           # 60 second snapshot
│   │   ├── trade-technical/SKILL.md       # Technical sub agent
│   │   ├── trade-fundamental/SKILL.md     # Fundamental sub agent
│   │   ├── trade-sentiment/SKILL.md       # Sentiment sub agent
│   │   ├── trade-sector/SKILL.md          # Sector analysis
│   │   ├── trade-compare/SKILL.md         # Head to head comparison
│   │   ├── trade-thesis/SKILL.md          # Investment thesis builder
│   │   ├── trade-options/SKILL.md         # Options strategies
│   │   ├── trade-earnings/SKILL.md        # Pre earnings positioning
│   │   ├── trade-portfolio/SKILL.md       # Portfolio analysis
│   │   ├── trade-risk/SKILL.md            # Risk assessment
│   │   ├── trade-screen/SKILL.md          # Stock screener
│   │   ├── trade-watchlist/SKILL.md       # Watchlist builder
│   │   ├── trade-report/SKILL.md          # Investment report
│   │   ├── trading-ideas/SKILL.md         # Equity research
│   │   └── queue/SKILL.md                 # Task queue processor
│   └── tools/                             # Python computation tools
│       ├── black_scholes.py               # Options pricing engine
│       ├── bond.py                        # Fixed income calculator
│       ├── dcf.py                         # DCF computation
│       ├── portfolio.py                   # Portfolio optimizer
│       ├── ratios.py                      # Financial ratios
│       ├── technicals.py                  # Technical indicators
│       ├── zscore.py                      # Credit scoring
│       └── inbox.py                       # Task queue manager
```

---

## Use Cases

| User | How to Use |
|------|-----------|
| **Day Traders** | `/trade technical` for support/resistance, `/trade quick` for pre market scans |
| **Swing Traders** | `/trade analyze` for multi dimensional scoring, `/trade thesis` for entry/exit plans |
| **Long Term Investors** | `financial-analysis` and `dcf-valuation` for intrinsic value, `ratio-analysis` for benchmarking |
| **Options Traders** | `options-pricer` for Greeks and strategies, `/trade options` for recommendations |
| **Portfolio Managers** | `portfolio-optimizer` for allocation, `risk-assessment` for VaR and stress testing |
| **Fixed Income** | `bond-analysis` for yield/duration, `credit-analysis` for credit scoring |
| **Investment Bankers** | `excel-lbo` for LBO models, `m-and-a-analysis` for deal evaluation |
| **Equity Research** | `financial-report` for sell side reports, `earnings-analyzer` for estimate tracking |
| **Macro Strategists** | `macro-dashboard` for economic indicators and recession probability |
| **Income Investors** | `dividend-analysis` for safety scoring and yield assessment |

---

## Conventions

- All monetary values use USD unless otherwise specified
- Percentages are displayed to 2 decimal places
- Large numbers use comma separation (e.g., 1,000,000)
- All analysis includes data sources and timestamps
- Risk metrics include confidence intervals
- Analysis is presented objectively without providing investment advice
- Every output includes appropriate disclaimers

---

## Data Sources

All analysis relies on publicly available data gathered via web search:

- **SEC Filings:** 10 K, 10 Q, 8 K, S 1, proxy statements via EDGAR
- **Market Data:** Real time pricing, volume, and technical indicators
- **Analyst Coverage:** Wall Street research, price target updates, consensus estimates
- **Economic Data:** Federal Reserve (FRED), BLS, BEA, Census Bureau
- **Fixed Income:** FINRA TRACE, Treasury yields, swap rates
- **Credit Ratings:** S&P, Moody's, Fitch (publicly available)
- **Options Data:** Options chains, implied volatility, unusual activity
- **News and Sentiment:** Financial media, regulatory announcements

---

## Contributing

Contributions are welcome. To add a new skill or improve an existing one:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-skill`
3. Add your skill under `.claude/skills/your-skill/SKILL.md`
4. Follow the existing skill format with YAML frontmatter, clear step by step framework, and structured output
5. Submit a pull request with a detailed description

---

## License

This project is licensed under the MIT License.

---

*Built for Claude Code. Institutional grade financial analysis, powered entirely by AI.*
