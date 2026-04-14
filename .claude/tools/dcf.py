#!/usr/bin/env python3
"""
DCF (Discounted Cash Flow) Valuation Calculator

Usage (explicit FCFs):
  python .claude/tools/dcf.py \
    --fcf 100,115,132,152,175 \
    --wacc 0.10 \
    --tgr 0.03 \
    --net-debt 200 \
    --shares 50

Usage (project FCFs from current FCF + growth rates):
  python .claude/tools/dcf.py \
    --base-fcf 100 \
    --growth 0.15,0.13,0.11,0.09,0.07 \
    --wacc 0.10 \
    --tgr 0.03 \
    --net-debt 200 \
    --shares 50

Add --sensitivity for a WACC × Terminal Growth Rate table.
Add --company "AAPL" for labeling.
"""

import argparse
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def npv(cash_flows, discount_rate):
    """Sum of discounted cash flows. cash_flows[0] is year 1."""
    total = 0.0
    for i, cf in enumerate(cash_flows, start=1):
        total += cf / (1 + discount_rate) ** i
    return total


def terminal_value(final_fcf, tgr, wacc):
    if wacc <= tgr:
        print("ERROR: WACC must be greater than terminal growth rate.", file=sys.stderr)
        sys.exit(1)
    return final_fcf * (1 + tgr) / (wacc - tgr)


def intrinsic_value(fcfs, wacc, tgr, net_debt, shares):
    pv_fcfs = npv(fcfs, wacc)
    tv = terminal_value(fcfs[-1], tgr, wacc)
    pv_tv = tv / (1 + wacc) ** len(fcfs)
    ev = pv_fcfs + pv_tv
    equity_val = ev - net_debt
    per_share = equity_val / shares if shares > 0 else 0
    return pv_fcfs, tv, pv_tv, ev, equity_val, per_share


def sensitivity_table(fcfs, base_wacc, base_tgr, net_debt, shares):
    wacc_range = [base_wacc - 0.02, base_wacc - 0.01, base_wacc, base_wacc + 0.01, base_wacc + 0.02]
    tgr_range  = [base_tgr - 0.01, base_tgr - 0.005, base_tgr, base_tgr + 0.005, base_tgr + 0.01]

    print("\n  SENSITIVITY TABLE — Intrinsic Value per Share")
    print("  (Rows = WACC, Columns = Terminal Growth Rate)\n")

    header = f"  {'WACC \\ TGR':>12}"
    for tgr in tgr_range:
        header += f"  {tgr*100:>7.2f}%"
    print(header)
    print("  " + "─" * (12 + len(tgr_range) * 10 + 4))

    for wacc in wacc_range:
        row = f"  {wacc*100:>10.2f}% "
        for tgr in tgr_range:
            try:
                _, _, _, _, _, ps = intrinsic_value(fcfs, wacc, tgr, net_debt, shares)
                row += f"  {ps:>7.2f}"
            except SystemExit:
                row += f"  {'N/A':>7}"
        print(row)
    print()


def main():
    parser = argparse.ArgumentParser(
        description="DCF Valuation Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    # FCF inputs — either explicit list or project from base
    parser.add_argument("--fcf",      type=str, default=None, help="Comma-separated explicit FCFs for projection years (e.g. 100,115,132)")
    parser.add_argument("--base-fcf", type=float, default=None, help="Current year FCF to project forward")
    parser.add_argument("--growth",   type=str, default=None,   help="Comma-separated annual FCF growth rates (e.g. 0.15,0.13,0.11,0.09,0.07)")

    # Valuation parameters
    parser.add_argument("--wacc",     type=float, required=True, help="WACC (e.g. 0.10 for 10%%)")
    parser.add_argument("--tgr",      type=float, required=True, help="Terminal growth rate (e.g. 0.03 for 3%%)")
    parser.add_argument("--net-debt", type=float, default=0,     help="Net debt = Total Debt - Cash (can be negative if net cash)")
    parser.add_argument("--shares",   type=float, default=1,     help="Diluted shares outstanding")

    # Optional
    parser.add_argument("--company",     type=str, default="",     help="Company name for display")
    parser.add_argument("--current-price", type=float, default=None, help="Current stock price (to compute upside/downside)")
    parser.add_argument("--sensitivity", action="store_true",       help="Print WACC x TGR sensitivity table")
    parser.add_argument("--currency",    type=str, default="$",     help="Currency symbol (default: $)")

    args = parser.parse_args()
    cur = args.currency
    label = f" — {args.company}" if args.company else ""

    # Build FCF list
    if args.fcf:
        fcfs = [float(x.strip()) for x in args.fcf.split(",")]
    elif args.base_fcf is not None and args.growth:
        rates = [float(x.strip()) for x in args.growth.split(",")]
        fcfs = []
        current = args.base_fcf
        for r in rates:
            current = current * (1 + r)
            fcfs.append(current)
    else:
        print("ERROR: Provide either --fcf or both --base-fcf and --growth.", file=sys.stderr)
        sys.exit(1)

    n = len(fcfs)
    pv_fcfs, tv, pv_tv, ev, equity_val, per_share = intrinsic_value(
        fcfs, args.wacc, args.tgr, args.net_debt, args.shares
    )

    print("=" * 62)
    print(f"  DCF VALUATION{label}")
    print(f"  WACC: {args.wacc*100:.2f}%  |  Terminal Growth: {args.tgr*100:.2f}%  |  {n}-Year Projection")
    print("=" * 62)

    print(f"\n  {'YEAR':<8} {'FCF':>14}  {'Discount Factor':>16}  {'PV of FCF':>12}")
    print("  " + "─" * 54)
    total_pv = 0.0
    for i, cf in enumerate(fcfs, start=1):
        df = 1 / (1 + args.wacc) ** i
        pv = cf * df
        total_pv += pv
        print(f"  {f'Year {i}':<8} {cur}{cf:>13,.1f}  {df:>16.4f}  {cur}{pv:>11,.1f}")

    print("  " + "─" * 54)
    print(f"  {'PV of FCFs':<8} {' ':>14}  {' ':>16}  {cur}{total_pv:>11,.1f}")

    df_tv = 1 / (1 + args.wacc) ** n
    print(f"\n  TERMINAL VALUE CALCULATION")
    print(f"  ─────────────────────────────────────────────────────")
    print(f"  Terminal FCF (Year {n} × (1+{args.tgr*100:.2f}%)):  {cur}{fcfs[-1]*(1+args.tgr):>10,.1f}")
    print(f"  Terminal Value  (TV = FCF × (1+g) / (WACC-g)):  {cur}{tv:>10,.1f}")
    print(f"  Discount Factor at Year {n}:                   {df_tv:>10.4f}")
    print(f"  PV of Terminal Value:                          {cur}{pv_tv:>10,.1f}")

    tv_pct = pv_tv / ev * 100 if ev != 0 else 0
    fcf_pct = total_pv / ev * 100 if ev != 0 else 0

    print(f"\n  ENTERPRISE VALUE BRIDGE")
    print(f"  ─────────────────────────────────────────────────────")
    print(f"  PV of FCFs:          {cur}{total_pv:>12,.1f}  ({fcf_pct:.1f}% of EV)")
    print(f"  PV of Terminal Value:{cur}{pv_tv:>12,.1f}  ({tv_pct:.1f}% of EV)")
    print(f"  Enterprise Value:    {cur}{ev:>12,.1f}")
    print(f"  Less: Net Debt:     ({cur}{args.net_debt:>11,.1f})")
    print(f"  Equity Value:        {cur}{equity_val:>12,.1f}")
    print(f"  Shares Outstanding:  {args.shares:>12,.1f}")

    print(f"\n{'=' * 62}")
    print(f"  INTRINSIC VALUE PER SHARE:  {cur}{per_share:>10.2f}")
    if args.current_price:
        updown = (per_share - args.current_price) / args.current_price * 100
        sign = "+" if updown >= 0 else ""
        print(f"  CURRENT PRICE:              {cur}{args.current_price:>10.2f}")
        print(f"  UPSIDE / DOWNSIDE:          {sign}{updown:.1f}%")
        verdict = "UNDERVALUED" if updown > 10 else ("OVERVALUED" if updown < -10 else "FAIRLY VALUED")
        print(f"  VERDICT:                    {verdict}")
    print("=" * 62)

    if args.sensitivity:
        sensitivity_table(fcfs, args.wacc, args.tgr, args.net_debt, args.shares)

    print("\n  ASSUMPTIONS & CAVEATS")
    print("  • DCF is highly sensitive to WACC and terminal growth rate assumptions.")
    print("  • Terminal value represents the value of cash flows beyond the projection period.")
    print(f"  • TV = {tv_pct:.1f}% of EV — {'HIGH: results very sensitive to terminal assumptions' if tv_pct > 70 else 'reasonable TV weighting'}.")
    print("  • This output is for analytical reference only — not investment advice.\n")


if __name__ == "__main__":
    main()
