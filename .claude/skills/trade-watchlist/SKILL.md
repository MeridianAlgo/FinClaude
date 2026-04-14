---
name: trade-watchlist
description: Build, score, and rank a stock watchlist. Takes a list of tickers and scores each on a simplified Trade Score, then ranks them by opportunity quality. Saves the watchlist to file. Use when the user wants to evaluate or rank a watchlist or runs /trade watchlist.
argument-hint: "[TICKER1,TICKER2,TICKER3,...] [optional: --update to refresh existing]"
allowed-tools:
  - WebSearch
  - WebFetch
  - Read
  - Write
---

# /trade watchlist — Ranked Watchlist Builder

You are a research analyst building and scoring a prioritized watchlist.

## Tickers: `$ARGUMENTS[0]`
## Mode: `$ARGUMENTS[1]` (blank = new watchlist, `--update` = refresh existing)

If no tickers provided, check if a watchlist file exists at `WATCHLIST.md` and load it. Otherwise ask for tickers.

---

## Step 1: Score Each Ticker (Rapid Scan)

For each ticker in the list, gather quickly:
- Current price vs 50D/200D MA (trend signal)
- RSI (14) (momentum)
- Forward P/E vs sector (valuation)
- Revenue growth YoY (growth)
- Analyst consensus (sentiment)
- 30-day performance (momentum)

Score each ticker 0-100 across 5 dimensions using a simplified scoring rubric:

| Dimension | Weight | Quick Criteria |
|-----------|--------|---------------|
| Technical | 25% | Price vs MAs, RSI, momentum |
| Fundamental | 25% | Valuation, growth, quality |
| Sentiment | 20% | Analyst consensus, recent actions |
| Risk | 15% | Beta, volatility level |
| Catalyst | 15% | Upcoming earnings, news, events |

---

## Step 2: Ranked Watchlist Table

```
WATCHLIST — [Date]
══════════════════════════════════════════════════════════════════════════
Rank | Ticker | Company           | Score | Grade | Signal    | Notes
─────┼────────┼───────────────────┼───────┼───────┼───────────┼──────────
 1   | [T]    | [Name]            | __    | A     | BUY       | [key reason]
 2   | [T]    | [Name]            | __    | A     | BUY       |
 3   | [T]    | [Name]            | __    | B     | HOLD      |
 4   | [T]    | [Name]            | __    | B     | HOLD      |
 5   | [T]    | [Name]            | __    | C     | CAUTION   |
...  | ...    | ...               | ...   | ...   | ...       | ...
══════════════════════════════════════════════════════════════════════════
```

---

## Step 3: Top 3 Opportunities (Deep Dive)

For the top 3 ranked stocks, provide a brief opportunity brief:

### #1: [TICKER] — Score: __/100
- **Why #1:** [Primary reason — e.g., "Strong uptrend + earnings revision momentum + cheap vs peers"]
- **Entry:** $____ | **Target:** $____ | **Stop:** $____
- **Catalyst:** [Next event, date]
- **Risk:** [Primary risk to watch]

### #2: [TICKER] — Score: __/100
[Brief version of above]

### #3: [TICKER] — Score: __/100
[Brief version of above]

---

## Step 4: Watchlist Health Check

```
WATCHLIST HEALTH
══════════════════════════════════
Total tickers:       ____
Buy/Hold/Caution:    __ / __ / __
Avg Score:           ____
Highest Score:       [TICKER] (____)
Lowest Score:        [TICKER] (____)

Sector Distribution:
  Tech: __% | Healthcare: __% | Financials: __% | Other: __%

Quality Signal:
  [Good opportunity set / Mixed signals / Limited opportunities]
```

---

## Step 5: Save Watchlist

Save the scored watchlist to `WATCHLIST.md` with format:

```markdown
# Watchlist — [Date]

| Rank | Ticker | Score | Signal | Last Updated |
|------|--------|-------|--------|-------------|
| 1 | [T] | __ | BUY | [Date] |
...

## Notes
[Any watchlist-level notes]
```

Confirm: "Watchlist saved to WATCHLIST.md — [N] stocks scored."

---

⚠️ Watchlist scores are point-in-time snapshots. Run `/trade watchlist --update` to refresh. For educational purposes only. Not financial advice.
