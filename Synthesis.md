Claude Equity Research
Built with Claude Code License: MIT Claude Code Required Status: Active

🤖 Built entirely with Claude Code - demonstrating AI-native development workflows for professional-grade financial tools.

Professional equity research and trading analysis powered by Claude AI, delivering institutional-grade investment insights with Goldman Sachs-style formatting and comprehensive risk assessment.

What It Does
Institutional-Grade Analysis: Generates professional equity research reports matching Wall Street standards
AI-Powered Intelligence: Leverages Claude AI for comprehensive fundamental and technical analysis
Real-Time Data Integration: Pulls live market data, earnings reports, and analyst coverage
Risk-Adjusted Recommendations: Provides buy/sell/hold ratings with specific price targets and position sizing
Advanced Market Intelligence: Includes options flow analysis, insider trading activity, and sector positioning
Key Features
Core Analysis Framework
Executive Summary: Investment thesis with price target and 12-month timeframe
Fundamental Analysis: Revenue growth, margins, peer comparisons, and forward estimates
Catalyst Analysis: Near-term and medium-term market drivers with specific dates
Valuation Models: Bull/base/bear scenarios with probability weighting
Risk Assessment: Company-specific and macro risks with position sizing guidance (1-5%)
Technical Context: Support/resistance levels, momentum indicators, and volume analysis
Enhanced Intelligence Features
Options Flow Analysis: Unusual activity, put/call ratios, implied volatility trends
Insider Activity Monitoring: Executive buying/selling patterns with dollar amounts
Sector Positioning: Rotation trends and relative strength vs market indices
ESG & Governance: Sustainability scores and regulatory compliance assessment
Professional Standards
Institutional Terminology: EBITDA, P/E ratios, EV/Sales, conviction levels
Probability Weighting: Bull/base/bear scenarios with percentage allocations
Legal Protection: Comprehensive disclaimers for educational use
Data Sourcing: Real-time web search with analyst firm citations
Installation & Setup
Prerequisites
Claude Code CLI (version 2.0.11 or higher)
Claude paid subscription (Pro, Team, or Enterprise)
Internet connection for real-time data retrieval
Installation via Claude Code Plugin (Recommended)
Quick Install - Interactive Menu:

# Step 1: Add the marketplace
/plugin marketplace add quant-sentiment-ai/claude-equity-research

# Step 2: Open the plugin menu
/plugin

# Step 3: Select "Browse Plugins" → find "claude-equity-research" → "Install now"
Alternative - Direct Install:

/plugin marketplace add quant-sentiment-ai/claude-equity-research
/plugin install claude-equity-research@quant-sentiment-ai
Verify Installation:

/help  # Confirm /trading-ideas command is listed
Start Analyzing:

/trading-ideas AAPL
/trading-ideas NVDA --detailed
💡 Tip: Restart Claude Code after installation for best results.

For comprehensive plugin documentation, see PLUGIN.md.

Manual Installation (Advanced)
Usage Examples
Basic Equity Analysis
/trading-ideas AAPL
Output: Comprehensive institutional research report with BUY/SELL/HOLD recommendation

Technology Sector Analysis
/trading-ideas NVDA
Features: AI/semiconductor sector positioning, relative valuation vs peers

Financial Services Analysis
/trading-ideas JPM
Includes: Interest rate sensitivity, regulatory environment, book value analysis

Growth Stock Analysis
/trading-ideas TSLA
Focus: Growth metrics, competitive positioning, volatility assessment

Sample Output Format
# APPLE INC (AAPL) - ENHANCED EQUITY RESEARCH

## EXECUTIVE SUMMARY
BUY with $250 price target (9% upside) over 12 months. Strong Q4 2024 
results driven by iPhone 16 launch and AI integration provide foundation 
for premium product cycle. Balanced risk-reward with established ecosystem moat.

## FUNDAMENTAL ANALYSIS
Q4 2024: Revenue $94.9B (+6% YoY), EPS $1.64 (+12% YoY). iPhone revenue 
$46.2B (~49% of total), Services +12% to $25B with recurring characteristics.

## VALUATION & PRICE TARGETS
Consensus: $242 (range $200-$280)
Bull case: $280 | Base case: $250 | Bear case: $200
Probability weighting: 25%/55%/20%

## RECOMMENDATION: BUY | Conviction: High | Price Target: $250
Command Reference
Command	Description	Output
/trading-ideas <TICKER>	Standard institutional analysis	8-section comprehensive report
/trading-ideas <TICKER> --detailed	Enhanced analysis with options flow	Extended technical and insider analysis
/trading-ideas --help	Show usage information	Command documentation
Repository Structure
claude-equity-research/
├── README.md                     # This file
├── LICENSE                       # MIT License
├── commands/
│   ├── trading-ideas.md          # Main Claude Code command
│   └── README.md                 # Command documentation
├── config/
│   ├── config.example.json       # Template configuration
│   └── prompts/                  # Analysis prompt templates
├── examples/
│   └── sample_reports/           # Example analyses (AAPL, HOOD, etc.)
├── docs/
│   ├── methodology.md            # Detailed analysis framework
│   ├── installation.md           # Setup instructions
│   └── customization.md          # Customization guide
├── utils/
│   ├── data_sources.md           # Data source documentation
│   └── validation.py             # Analysis validation tools
└── tests/
    └── test_command.py           # Command functionality tests
Analysis Methodology
Our research framework combines:

Quantitative Analysis
Financial Statements: Revenue, margins, cash flow analysis
Valuation Models: Multiple approaches (DCF, comparable company, precedent transaction)
Technical Indicators: Support/resistance, momentum, relative strength
Options Analytics: Implied volatility, unusual activity, sentiment indicators
Qualitative Assessment
Competitive Positioning: Market share, competitive advantages, moat analysis
Management Quality: Track record, capital allocation, strategic vision
Regulatory Environment: Industry-specific risks, compliance issues
ESG Factors: Environmental, social, governance considerations
Risk Management
Scenario Analysis: Bull/base/bear cases with probability weighting
Position Sizing: Risk-adjusted allocation recommendations (1-5% typical)
Stop-Loss Guidance: Downside protection levels
Correlation Analysis: Portfolio diversification considerations
Data Sources
Financial Data: SEC filings, earnings reports, company guidance
Market Data: Real-time pricing, volume, technical indicators
Analyst Coverage: Wall Street research, price target updates
News & Sentiment: Financial media, regulatory announcements
Options Data: Unusual activity, implied volatility, positioning
Insider Activity: Form 4 filings, executive transactions
Professional Disclaimers
⚠️ Important Legal Notice
This tool is designed for educational and research purposes only. All analysis and recommendations are:

Not financial advice - For informational purposes only
Not personalized - Does not consider individual circumstances
Historical data based - Past performance doesn't guarantee future results
Requiring due diligence - Users must conduct independent research
Risk warning included - All investments carry risk of loss
Risk Warnings
Stock prices are volatile and unpredictable
AI analysis may contain errors or biases
Market conditions change rapidly
Regulatory and company-specific risks may not be fully captured
Position sizing recommendations are general guidelines only
Professional Consultation
Always consult with qualified financial professionals before making investment decisions. This tool does not replace professional financial advice.

Contributing
We welcome contributions! Please see our Contributing Guidelines:

Development Areas
Enhanced data source integration
Improved technical analysis algorithms
Additional sector-specific metrics
ESG scoring improvements
Risk model enhancements
Code Contributions
# Fork the repository
git fork https://github.com/quant-sentiment-ai/claude-equity-research

# Create feature branch
git checkout -b feature/your-enhancement

# Submit pull request with detailed description
Star History
Star History Chart

License
This project is licensed under the MIT License - see the LICENSE file for details.

Support & Community
📖 Documentation
🐛 Report Issues
💬 Discussions
🔄 Changelog
Acknowledgments
Built for Claude Code - Anthropic's official CLI
Inspired by institutional equity research standards
Community-driven development and feedback
Remember: This tool provides educational insights only. Always conduct your own due diligence and consult qualified financial professionals before making investment decisions. Past performance does not guarantee future results.


---

rading Analyst for Claude Code. Run full stock analyses with 5 parallel agents, build investment theses,
assess risk, screen for opportunities, analyze options, and produce professional PDF reports — 16 skills, 5 agents, one command.

License: MIT 16 Skills 5 Agents Options Analysis Python 3.8+ PDF Reports

WARNING: This tool is for educational and research purposes only. It is NOT financial advice. It does NOT execute trades. It does NOT manage money. Always do your own due diligence and consult a licensed financial advisor before making investment decisions.

Quick Start
curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/ai-trading-claude/main/install.sh | bash
That's it. One command installs all 16 skills, 5 agents, and the PDF generation scripts.

What Is This?
AI Trading Analyst is a research and analysis tool built as Claude Code skills. It is not a trading bot. It does not connect to brokerages. It does not execute trades.

What it does: takes a ticker symbol and runs a comprehensive multi-dimensional analysis using 5 parallel AI agents — technical, fundamental, sentiment, risk, and thesis — then produces a composite Trade Score (0-100) with a clear signal (Strong Buy / Buy / Hold / Caution / Avoid).

Run /trade analyze AAPL and 5 AI agents launch in parallel to produce a complete investment research report.

No API keys. No brokerage accounts. No financial data subscriptions. Just Claude Code.

Architecture
                         /trade analyze <ticker>
                                 |
                   ┌─────────────┼─────────────┐
                   |             |             |
             ┌─────┴──────┐ ┌───┴─────┐ ┌─────┴──────┐
             | trade-      | | trade-  | | trade-     |
             | technical   | | funda-  | | sentiment  |
             | agent       | | mental  | | agent      |
             | (price,     | | agent   | | (news,     |
             |  patterns,  | | (value, | |  social,   |
             |  indicators)| |  growth)| |  analysts) |
             └─────────────┘ └────────┘ └────────────┘
                   |             |             |
             ┌─────┴──────┐ ┌───┴─────┐
             | trade-risk  | | trade-  |
             | agent       | | thesis  |
             | (volatility,| | agent   |
             |  sizing,    | | (bull/  |
             |  drawdown)  | |  bear,  |
             |             | |  entry) |
             └─────────────┘ └────────┘
                   |             |             |
                   └─────────────┼─────────────┘
                                 |
                   ┌─────────────┴─────────────┐
                   |   Composite Trade Score    |
                   |   (0-100) + Grade + Signal |
                   |   + PDF Investment Report  |
                   └───────────────────────────┘
All 16 Commands
Analysis & Research
Command	What It Does
/trade analyze <ticker>	Flagship — Full stock analysis with 5 parallel agents. Returns Trade Score (0-100), technical levels, fundamental metrics, sentiment reading, risk profile, investment thesis, and entry/exit plan.
/trade quick <ticker>	60-second stock snapshot — price, trend, key metrics, signal. No subagents.
/trade technical <ticker>	Technical analysis — price action, chart patterns, indicators, support/resistance levels.
/trade fundamental <ticker>	Fundamental analysis — financials, valuation metrics, competitive moat, growth trajectory.
/trade sentiment <ticker>	News and social sentiment — analyst ratings, insider activity, social buzz, news tone.
/trade sector <sector>	Sector rotation and momentum — relative strength, fund flows, top/bottom performers.
Thesis & Strategy
Command	What It Does
/trade thesis <ticker>	Complete investment thesis — bull/bear cases, catalysts, entry/exit strategy with price levels.
/trade compare <t1> <t2>	Head-to-head stock comparison across all dimensions with a winner recommendation.
/trade options <ticker>	Options strategy recommendations — covered calls, spreads, protective puts based on outlook.
/trade earnings <ticker>	Pre-earnings analysis — expected move, historical reactions, positioning strategy.
Portfolio & Risk
Command	What It Does
/trade portfolio	Portfolio analysis — correlation matrix, sector exposure, rebalancing recommendations.
/trade risk <ticker>	Risk assessment — position sizing, max drawdown, scenario analysis, risk/reward ratio.
/trade screen <criteria>	Stock screener — filter by strategy (momentum, value, dividend, growth, etc.).
/trade watchlist	Build and update a scored watchlist with ranked opportunities.
Reporting
Command	What It Does
/trade report-pdf	Professional 6-page PDF investment report with score gauges, charts, and thesis.
Scoring Methodology
The Trade Score (0-100) is a weighted composite of 5 dimensions:

Category	Weight	What It Measures
Technical Strength	25%	Trend, momentum, volume, pattern quality, support/resistance
Fundamental Quality	25%	Valuation, growth, profitability, balance sheet, moat
Sentiment & Momentum	20%	News tone, social buzz, analyst consensus, insider signals
Risk Profile	15%	Volatility, drawdown potential, correlation, liquidity
Thesis Conviction	15%	Catalyst clarity, timeline, asymmetry, edge identification
Grade & Signal Interpretation
Score	Grade	Signal	Meaning
85-100	A+	Strong Buy	High conviction across all dimensions
70-84	A	Buy	Favorable setup with manageable risks
55-69	B	Hold	Mixed signals, wait for confirmation
40-54	C	Caution	No clear edge, stay on sidelines
25-39	D	Caution	Significant headwinds or overvaluation
0-24	F	Avoid	Major red flags across multiple dimensions
Sample Output
/trade analyze AAPL
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

Saved: TRADE-ANALYSIS-AAPL.md
/trade quick NVDA
⚡ TRADE SNAPSHOT — NVDA (NVIDIA Corp.)

  Score: 81/100 (A) — BUY
  Price: $892.40 (+2.3% today)
  Trend: Strong uptrend, above all major MAs

  ✓ Revenue growth +122% YoY (AI demand)
  ✓ RSI 58 — bullish, not overbought
  ✓ Institutional accumulation pattern

  ✗ P/E 65x — premium valuation
  ✗ High beta (1.7) — volatile
  ✗ Concentration risk in AI capex cycle

  Run /trade analyze NVDA for the full multi-agent analysis
Use Cases
Day Traders
Use /trade technical for real-time support/resistance levels, indicator readings, and pattern recognition. Run /trade quick for fast pre-market scans.

Swing Traders
Run /trade analyze for multi-dimensional analysis. Use /trade thesis to build entry/exit plans with specific price levels and timeframes.

Long-Term Investors
Focus on /trade fundamental for deep valuation and moat analysis. Use /trade compare to evaluate alternatives. Run /trade portfolio for allocation guidance.

Options Traders
Use /trade options for strategy recommendations based on the current setup. Combine with /trade earnings for pre-earnings positioning and expected move analysis.

Portfolio Managers
Run /trade portfolio for correlation analysis and rebalancing suggestions. Use /trade screen to find new opportunities. Build ranked watchlists with /trade watchlist.

Installation
Prerequisites
Claude Code (with an active Anthropic API key)
Python 3.8+ (for PDF generation only)
reportlab — pip3 install reportlab (for PDF generation only)
One-Line Install
curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/ai-trading-claude/main/install.sh | bash
Manual Install
git clone https://github.com/zubair-trabzada/ai-trading-claude.git
cd ai-trading-claude
chmod +x install.sh
./install.sh
Uninstall
curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/ai-trading-claude/main/uninstall.sh | bash
Or run locally:

./uninstall.sh
Project Structure
ai-trading-claude/
├── trade/
│   └── SKILL.md                         # Main orchestrator (command router)
├── skills/
│   ├── trade-analyze/SKILL.md           # Full analysis launcher
│   ├── trade-technical/SKILL.md         # Technical analysis
│   ├── trade-fundamental/SKILL.md       # Fundamental analysis
│   ├── trade-sentiment/SKILL.md         # Sentiment analysis
│   ├── trade-sector/SKILL.md            # Sector rotation
│   ├── trade-compare/SKILL.md           # Stock comparison
│   ├── trade-thesis/SKILL.md            # Investment thesis
│   ├── trade-options/SKILL.md           # Options strategies
│   ├── trade-portfolio/SKILL.md         # Portfolio analysis
│   ├── trade-risk/SKILL.md              # Risk assessment
│   ├── trade-screen/SKILL.md            # Stock screener
│   ├── trade-earnings/SKILL.md          # Earnings analysis
│   ├── trade-watchlist/SKILL.md         # Watchlist builder
│   ├── trade-report-pdf/SKILL.md        # PDF report generator
│   └── trade-quick/SKILL.md             # 60-second snapshot
├── agents/
│   ├── trade-technical.md               # Technical analysis agent
│   ├── trade-fundamental.md             # Fundamental analysis agent
│   ├── trade-sentiment.md               # Sentiment analysis agent
│   ├── trade-risk.md                    # Risk assessment agent
│   └── trade-thesis.md                  # Thesis synthesis agent
├── scripts/
│   └── generate_trade_pdf.py            # PDF generation (ReportLab)
├── install.sh                           # One-line installer
├── uninstall.sh                         # Clean uninstaller
├── requirements.txt                     # Python dependencies
└── README.md
Disclaimer
This tool is for educational and research purposes only. It is NOT financial advice. It does NOT execute trades, manage portfolios, or connect to any brokerage. All analysis is based on publicly available information gathered via web search at the time of the report. Markets are inherently unpredictable. Past performance does not guarantee future results. Always do your own due diligence and consult a licensed financial advisor before making any investment decisions. The creators of this tool accept no liability for any financial losses incurred.

Part of the Claude Code Skills Series
AI Marketing Suite · AI Sales Team · AI Legal Assistant · AI Reputation Manager · GEO/SEO Optimizer · AI Ads Strategist · AI Trading Analyst

Learn How to Build AI Tools with Claude Code

License: MIT


---


Excel Analyst Pro
Professional financial modeling toolkit for Claude Code with auto-invoked Skills and Excel MCP integration.

Build DCF models, LBO analysis, variance reports, and pivot tables using natural language. No formulas to remember, no manual Excel work.

Features
DCF Modeler: Discounted cash flow valuation models with projections, WACC, and sensitivity analysis
LBO Modeler: Leveraged buyout models with debt schedules, cash flow waterfalls, and IRR calculations
Variance Analyzer: Budget vs actual analysis with flagging, commentary, and executive summaries
Pivot Wizard: Pivot tables and charts from raw data using natural language
Installation
Prerequisites
Claude Code 1.0+
Node.js 18+
Install
/plugin install excel-analyst-pro
This automatically configures @negokaz/excel-mcp-server and loads all 4 Skills.

Usage
DCF Valuation
"Create a DCF model for Tesla with $96.8B revenue and 25% growth"
Produces a 4-sheet Excel workbook: Assumptions, FCF Projections, Valuation, Sensitivity Analysis.

LBO Analysis
"Build an LBO model for a $50M EBITDA software company at 12x"
Produces a 6-sheet Excel workbook: Transaction Summary, Sources & Uses, Operating Model, Debt Schedule, Returns Analysis, Debt Covenants.

Variance Analysis
"Analyze Q1 budget vs actual"
Produces a 3-sheet Excel report: Variance Summary, Executive Summary, Trend Analysis.

Pivot Tables
"Show sales by region and product category"
Creates pivot tables with charts, calculated fields, and conditional formatting.

Plugin Architecture
excel-analyst-pro/
├── plugin.json
├── skills/
│   ├── excel-dcf-modeler/
│   │   ├── SKILL.md
│   │   ├── evals/evals.json
│   │   └── references/REFERENCE.md
│   ├── excel-lbo-modeler/
│   │   ├── SKILL.md
│   │   ├── evals/evals.json
│   │   └── references/REFERENCE.md
│   ├── excel-pivot-wizard/
│   │   ├── SKILL.md
│   │   ├── evals/evals.json
│   │   └── references/REFERENCE.md
│   └── excel-variance-analyzer/
│       ├── SKILL.md
│       ├── evals/evals.json
│       └── references/REFERENCE.md
└── slash-commands/
    ├── build-dcf.md
    ├── build-lbo.md
    └── analyze-variance.md
MCP Server
Uses @negokaz/excel-mcp-server for all Excel operations. No Microsoft Excel installation required. All processing is local.

License
Intent Solutions Proprietary - see LICENSE for details.

For commercial licensing: jeremy@intentsolutions.io


---