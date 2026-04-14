#!/usr/bin/env python3
"""
Financial Ratios Calculator
Computes all major financial ratios across liquidity, leverage, profitability, efficiency, and valuation.

Usage:
  python .claude/tools/ratios.py \
    --revenue 5000 --gross-profit 2000 --ebitda 1200 --ebit 900 --net-income 650 \
    --interest-expense 80 --tax-rate 0.21 \
    --total-assets 8000 --total-equity 3500 --total-debt 2500 \
    --cash 800 --current-assets 2200 --current-liabilities 1100 \
    --inventory 400 --receivables 600 --payables 500 \
    --ocf 950 --fcf 650 --capex 300 \
    --shares 200 --price 45 \
    --company "Example Corp"
"""

import argparse
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def ratio(num, denom, default=None):
    """Safe ratio computation — returns default if denom is 0."""
    if denom is None or denom == 0:
        return default
    if num is None:
        return default
    return num / denom


def pct(num, denom):
    r = ratio(num, denom)
    return r * 100 if r is not None else None


def fmt_ratio(value, decimals=2, suffix="x"):
    if value is None:
        return "N/A"
    return f"{value:.{decimals}f}{suffix}"


def fmt_pct(value, decimals=2):
    if value is None:
        return "N/A"
    return f"{value:.{decimals}f}%"


def fmt_dollar(value, decimals=1):
    if value is None:
        return "N/A"
    return f"${value:,.{decimals}f}"


def rate_ratio(value, low_good, high_good, label=""):
    """Rate a ratio: ✓ in range, ▲ above, ▼ below."""
    if value is None:
        return "N/A"
    if low_good is not None and value < low_good:
        return "▼ LOW"
    elif high_good is not None and value > high_good:
        return "▲ HIGH"
    else:
        return "✓ OK"


def print_section(title):
    print(f"\n  {title}")
    print(f"  {'─'*62}")
    print(f"  {'Metric':<42} {'Value':>10}  {'Note'}")
    print(f"  {'─'*62}")


def print_row(name, value_str, note=""):
    print(f"  {name:<42} {value_str:>10}  {note}")


def main():
    p = argparse.ArgumentParser(
        description="Financial Ratios Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    # Income statement
    p.add_argument("--revenue",          type=float, default=None)
    p.add_argument("--gross-profit",     type=float, default=None)
    p.add_argument("--ebitda",           type=float, default=None)
    p.add_argument("--ebit",             type=float, default=None, help="EBIT / Operating Income")
    p.add_argument("--net-income",       type=float, default=None)
    p.add_argument("--interest-expense", type=float, default=None)
    p.add_argument("--tax-rate",         type=float, default=None, help="e.g. 0.21 for 21%%")
    p.add_argument("--sga",              type=float, default=None, help="SG&A expense")
    p.add_argument("--rnd",              type=float, default=None, help="R&D expense")
    p.add_argument("--da",               type=float, default=None, help="Depreciation & Amortization")

    # Balance sheet
    p.add_argument("--total-assets",       type=float, default=None)
    p.add_argument("--total-equity",       type=float, default=None)
    p.add_argument("--total-debt",         type=float, default=None)
    p.add_argument("--cash",               type=float, default=None)
    p.add_argument("--current-assets",     type=float, default=None)
    p.add_argument("--current-liabilities",type=float, default=None)
    p.add_argument("--inventory",          type=float, default=None)
    p.add_argument("--receivables",        type=float, default=None)
    p.add_argument("--payables",           type=float, default=None)
    p.add_argument("--ppe",                type=float, default=None, help="Net PP&E")
    p.add_argument("--goodwill",           type=float, default=None)
    p.add_argument("--intangibles",        type=float, default=None)

    # Cash flow
    p.add_argument("--ocf",   type=float, default=None, help="Operating Cash Flow")
    p.add_argument("--fcf",   type=float, default=None, help="Free Cash Flow")
    p.add_argument("--capex", type=float, default=None, help="Capital Expenditures")

    # Market / valuation
    p.add_argument("--shares",    type=float, default=None, help="Diluted shares outstanding")
    p.add_argument("--price",     type=float, default=None, help="Current stock price")
    p.add_argument("--dividends", type=float, default=None, help="Total dividends paid")
    p.add_argument("--dps",       type=float, default=None, help="Dividends per share")

    # Context
    p.add_argument("--company", type=str, default="", help="Company name")
    p.add_argument("--sector",  type=str, default="", help="Sector (for context)")

    args = p.parse_args()
    label = f" — {args.company}" if args.company else ""

    # Derived values
    net_debt = (args.total_debt - args.cash) if (args.total_debt is not None and args.cash is not None) else None
    market_cap = (args.shares * args.price) if (args.shares is not None and args.price is not None) else None
    ev = (market_cap + (net_debt or 0)) if market_cap is not None else None
    quick_assets = ((args.current_assets or 0) - (args.inventory or 0)) if args.current_assets is not None else None
    total_liabilities = ((args.total_assets or 0) - (args.total_equity or 0)) if (args.total_assets and args.total_equity) else None
    nopat = (args.ebit * (1 - (args.tax_rate or 0.21))) if args.ebit is not None else None
    invested_capital = ((args.total_equity or 0) + (args.total_debt or 0)) if (args.total_equity or args.total_debt) else None
    eps = ratio(args.net_income, args.shares)

    print("=" * 64)
    print(f"  FINANCIAL RATIOS ANALYSIS{label}")
    if args.sector:
        print(f"  Sector: {args.sector}")
    print("=" * 64)

    # ─── LIQUIDITY ───
    curr = ratio(args.current_assets, args.current_liabilities)
    quick = ratio(quick_assets, args.current_liabilities)
    cash_r = ratio(args.cash, args.current_liabilities)

    print_section("1. LIQUIDITY RATIOS")
    print_row("Current Ratio",    fmt_ratio(curr), rate_ratio(curr, 1.5, 3.0) + "  (healthy: 1.5–3.0x)")
    print_row("Quick Ratio",      fmt_ratio(quick), rate_ratio(quick, 1.0, 2.5) + "  (healthy: ≥1.0x)")
    print_row("Cash Ratio",       fmt_ratio(cash_r), rate_ratio(cash_r, 0.2, 1.0) + "  (healthy: ≥0.2x)")
    print_row("Working Capital",  fmt_dollar((args.current_assets or 0) - (args.current_liabilities or 0)) if (args.current_assets and args.current_liabilities) else "N/A")
    if args.ocf and args.current_liabilities:
        print_row("Operating CF Ratio", fmt_ratio(ratio(args.ocf, args.current_liabilities)), "OCF / Current Liabilities")

    # ─── LEVERAGE ───
    de = ratio(args.total_debt, args.total_equity)
    da_r = ratio(args.total_debt, args.total_assets)
    interest_cov = ratio(args.ebit, args.interest_expense)
    ebitda_cov = ratio(args.ebitda, args.interest_expense)
    nd_ebitda = ratio(net_debt, args.ebitda)
    debt_ebitda = ratio(args.total_debt, args.ebitda)

    print_section("2. LEVERAGE / SOLVENCY RATIOS")
    print_row("Debt / Equity",          fmt_ratio(de),          rate_ratio(de, None, 2.0) + "  (conservative: <1.0x)")
    print_row("Debt / Total Assets",    fmt_ratio(da_r),        rate_ratio(da_r, None, 0.5) + "  (healthy: <0.5x)")
    print_row("Net Debt / EBITDA",      fmt_ratio(nd_ebitda),   rate_ratio(nd_ebitda, None, 3.0) + "  (healthy: <2.5x)")
    print_row("Total Debt / EBITDA",    fmt_ratio(debt_ebitda), "gross leverage")
    print_row("EBIT / Interest (Coverage)", fmt_ratio(interest_cov),  rate_ratio(interest_cov, 3.0, None) + "  (healthy: >3.0x)")
    print_row("EBITDA / Interest",      fmt_ratio(ebitda_cov),  rate_ratio(ebitda_cov, 4.0, None) + "  (healthy: >4.0x)")
    if args.ocf and args.total_debt:
        fcf_to_debt = ratio(args.fcf or args.ocf, args.total_debt)
        print_row("FCF / Total Debt",   fmt_ratio(fcf_to_debt), "repayment capacity")
    if net_debt is not None:
        print_row("Net Debt",           fmt_dollar(net_debt), "Debt – Cash")

    # ─── PROFITABILITY ───
    gross_m  = pct(args.gross_profit, args.revenue)
    ebitda_m = pct(args.ebitda, args.revenue)
    ebit_m   = pct(args.ebit, args.revenue)
    net_m    = pct(args.net_income, args.revenue)
    roe      = pct(args.net_income, args.total_equity)
    roa      = pct(args.net_income, args.total_assets)
    roic     = pct(nopat, invested_capital) if invested_capital and nopat else None
    roce     = pct(args.ebit, invested_capital) if invested_capital else None
    fcf_m    = pct(args.fcf, args.revenue)
    ocf_m    = pct(args.ocf, args.revenue)
    sga_r    = pct(args.sga, args.revenue)
    rnd_r    = pct(args.rnd, args.revenue)

    print_section("3. PROFITABILITY RATIOS")
    print_row("Gross Margin",        fmt_pct(gross_m),  "Gross Profit / Revenue")
    print_row("EBITDA Margin",       fmt_pct(ebitda_m), "EBITDA / Revenue")
    print_row("EBIT / Operating Margin", fmt_pct(ebit_m), "EBIT / Revenue")
    print_row("Net Profit Margin",   fmt_pct(net_m),    "Net Income / Revenue")
    print_row("FCF Margin",          fmt_pct(fcf_m),    "Free Cash Flow / Revenue")
    print_row("OCF Margin",          fmt_pct(ocf_m),    "Operating CF / Revenue")
    print_row("ROE",                 fmt_pct(roe),      rate_ratio(roe, 10, None) + "  (strong: >15%)")
    print_row("ROA",                 fmt_pct(roa),      "Net Income / Total Assets")
    print_row("ROIC",                fmt_pct(roic),     "NOPAT / Invested Capital")
    print_row("ROCE",                fmt_pct(roce),     "EBIT / Invested Capital")
    if args.sga:  print_row("SG&A / Revenue",    fmt_pct(sga_r))
    if args.rnd:  print_row("R&D / Revenue",     fmt_pct(rnd_r))

    # Quality check
    if args.ocf and args.net_income:
        quality = ratio(args.ocf, args.net_income)
        note = "✓ High quality earnings" if quality > 1.0 else "⚠ Earnings > OCF (watch accruals)"
        print_row("Earnings Quality (OCF/NI)", fmt_ratio(quality), note)

    # ─── EFFICIENCY ───
    asset_turn = ratio(args.revenue, args.total_assets)
    inv_turn   = ratio(args.revenue, args.inventory) if args.inventory else None
    inv_days   = (365 / inv_turn) if inv_turn else None
    rec_turn   = ratio(args.revenue, args.receivables) if args.receivables else None
    rec_days   = (365 / rec_turn) if rec_turn else None
    pay_turn   = ratio(args.revenue, args.payables) if args.payables else None
    pay_days   = (365 / pay_turn) if pay_turn else None
    ccc = None
    if rec_days is not None and inv_days is not None and pay_days is not None:
        ccc = rec_days + inv_days - pay_days
    capex_r = pct(args.capex, args.revenue)
    da_r_pct = pct(args.da, args.revenue)

    print_section("4. EFFICIENCY / ACTIVITY RATIOS")
    print_row("Asset Turnover",          fmt_ratio(asset_turn), "Revenue / Total Assets")
    if inv_turn:  print_row("Inventory Turnover",  fmt_ratio(inv_turn), f"DSI: {inv_days:.0f} days" if inv_days else "")
    if rec_turn:  print_row("Receivables Turnover", fmt_ratio(rec_turn), f"DSO: {rec_days:.0f} days" if rec_days else "")
    if pay_turn:  print_row("Payables Turnover",   fmt_ratio(pay_turn), f"DPO: {pay_days:.0f} days" if pay_days else "")
    if ccc is not None: print_row("Cash Conversion Cycle", f"{ccc:.0f} days", "DSO + DSI – DPO (lower is better)")
    if capex_r:   print_row("CapEx / Revenue",     fmt_pct(capex_r))
    if da_r_pct:  print_row("D&A / Revenue",       fmt_pct(da_r_pct))
    if args.ppe and args.da and args.da > 0:
        ppe_ratio = args.ppe / args.da
        print_row("PP&E / D&A (avg asset age)", fmt_ratio(ppe_ratio), f"~{ppe_ratio:.0f} years avg remaining life")

    # ─── VALUATION ───
    pe   = ratio(args.price, eps) if args.price and eps else None
    pb   = ratio(args.price, ratio(args.total_equity, args.shares)) if (args.price and args.total_equity and args.shares) else None
    ps   = ratio(market_cap, args.revenue) if market_cap and args.revenue else None
    ev_ebitda = ratio(ev, args.ebitda) if ev and args.ebitda else None
    ev_ebit   = ratio(ev, args.ebit)   if ev and args.ebit else None
    ev_rev    = ratio(ev, args.revenue) if ev and args.revenue else None
    fcf_yield = pct(args.fcf, market_cap) if args.fcf and market_cap else None
    div_yield = pct(args.dps, args.price) if args.dps and args.price else None
    payout    = pct(args.dividends, args.net_income) if args.dividends and args.net_income else None

    print_section("5. VALUATION RATIOS")
    if market_cap: print_row("Market Capitalization", fmt_dollar(market_cap))
    if ev:         print_row("Enterprise Value",       fmt_dollar(ev))
    print_row("P/E Ratio",        fmt_ratio(pe),       rate_ratio(pe, 5, 40))
    print_row("P/Book",           fmt_ratio(pb),       "Price / Book Value per Share")
    print_row("P/Sales (EV/Rev)", fmt_ratio(ev_rev),   "EV / Revenue")
    print_row("EV/EBITDA",        fmt_ratio(ev_ebitda), rate_ratio(ev_ebitda, 5, 20) + "  (reasonable: 8–15x)")
    print_row("EV/EBIT",          fmt_ratio(ev_ebit),  "EV / EBIT")
    if eps:        print_row("EPS (Diluted)",    fmt_dollar(eps, 2))
    if fcf_yield:  print_row("FCF Yield",        fmt_pct(fcf_yield), "FCF / Market Cap")
    if div_yield:  print_row("Dividend Yield",   fmt_pct(div_yield))
    if payout:     print_row("Payout Ratio",     fmt_pct(payout),    rate_ratio(payout, None, 75))

    print(f"\n{'='*64}")
    print(f"  NOTE: Ratios are most meaningful when benchmarked against:")
    print(f"  • Industry peers (same sector, similar size)")
    print(f"  • Historical trend for the same company")
    print(f"  • Debt covenant thresholds if applicable")
    print(f"  This output is for analytical reference only — not investment advice.\n")


if __name__ == "__main__":
    main()
