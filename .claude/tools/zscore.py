#!/usr/bin/env python3
"""
Altman Z-Score Calculator
Computes Z-Score for public companies and Z'-Score for private companies.

Usage (public):
  python .claude/tools/zscore.py --wc 500 --re 200 --ebit 150 --mkcap 1000 --td 800 --rev 2000 --ta 3000

Usage (private):
  python .claude/tools/zscore.py --wc 500 --re 200 --ebit 150 --bveq 800 --td 800 --rev 2000 --ta 3000 --private

All dollar inputs in the same unit (e.g., all $M or all $B — just be consistent).
"""

import argparse
import sys

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def compute_public(wc, re, ebit, mkcap, td, rev, ta):
    if ta == 0 or td == 0:
        print("ERROR: Total assets and total debt must be non-zero.", file=sys.stderr)
        sys.exit(1)
    x1 = wc / ta
    x2 = re / ta
    x3 = ebit / ta
    x4 = mkcap / td
    x5 = rev / ta
    z = 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5
    return z, x1, x2, x3, x4, x5


def compute_private(wc, re, ebit, bveq, td, rev, ta):
    if ta == 0 or td == 0:
        print("ERROR: Total assets and total debt must be non-zero.", file=sys.stderr)
        sys.exit(1)
    x1 = wc / ta
    x2 = re / ta
    x3 = ebit / ta
    x4 = bveq / td
    x5 = rev / ta
    z = 0.717 * x1 + 0.847 * x2 + 3.107 * x3 + 0.420 * x4 + 0.998 * x5
    return z, x1, x2, x3, x4, x5


def zone_public(z):
    if z > 2.99:
        return "SAFE ZONE", "Low default risk — financially healthy"
    elif z > 1.81:
        return "GREY ZONE", "Moderate risk — monitor closely"
    else:
        return "DISTRESS ZONE", "High default risk — potential bankruptcy"


def zone_private(z):
    if z > 2.90:
        return "SAFE ZONE", "Low default risk"
    elif z > 1.23:
        return "GREY ZONE", "Moderate risk — monitor closely"
    else:
        return "DISTRESS ZONE", "High default risk — potential bankruptcy"


def bar(value, low, high, width=30):
    """ASCII progress bar for a value between low and high."""
    clamped = max(low, min(high, value))
    filled = int((clamped - low) / (high - low) * width)
    return "[" + "█" * filled + "░" * (width - filled) + "]"


def main():
    parser = argparse.ArgumentParser(
        description="Altman Z-Score / Z'-Score Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--wc",    type=float, required=True, help="Working Capital (Current Assets - Current Liabilities)")
    parser.add_argument("--re",    type=float, required=True, help="Retained Earnings")
    parser.add_argument("--ebit",  type=float, required=True, help="Earnings Before Interest and Taxes")
    parser.add_argument("--mkcap", type=float, default=None,  help="[Public] Market Capitalization")
    parser.add_argument("--bveq",  type=float, default=None,  help="[Private] Book Value of Equity")
    parser.add_argument("--td",    type=float, required=True, help="Total Debt (short-term + long-term)")
    parser.add_argument("--rev",   type=float, required=True, help="Revenue / Net Sales")
    parser.add_argument("--ta",    type=float, required=True, help="Total Assets")
    parser.add_argument("--private", action="store_true",     help="Use Z'-Score model for private companies")
    parser.add_argument("--company", type=str, default="",    help="Company name (optional, for display)")

    args = parser.parse_args()

    label = f" — {args.company}" if args.company else ""

    print("=" * 60)
    print(f"  ALTMAN Z-SCORE ANALYSIS{label}")
    print(f"  Model: {'Z\'-Score (Private)' if args.private else 'Z-Score (Public)'}")
    print("=" * 60)

    print("\n  INPUT VARIABLES")
    print("  " + "-" * 46)
    print(f"  {'Working Capital':<30} {args.wc:>12,.1f}")
    print(f"  {'Retained Earnings':<30} {args.re:>12,.1f}")
    print(f"  {'EBIT':<30} {args.ebit:>12,.1f}")
    if args.private:
        bveq = args.bveq if args.bveq is not None else 0.0
        print(f"  {'Book Value of Equity':<30} {bveq:>12,.1f}")
    else:
        mkcap = args.mkcap if args.mkcap is not None else 0.0
        print(f"  {'Market Capitalization':<30} {mkcap:>12,.1f}")
    print(f"  {'Total Debt':<30} {args.td:>12,.1f}")
    print(f"  {'Revenue':<30} {args.rev:>12,.1f}")
    print(f"  {'Total Assets':<30} {args.ta:>12,.1f}")

    print("\n  VARIABLE COMPONENTS")
    print("  " + "-" * 56)

    if args.private:
        bveq = args.bveq if args.bveq is not None else 0.0
        z, x1, x2, x3, x4, x5 = compute_private(args.wc, args.re, args.ebit, bveq, args.td, args.rev, args.ta)
        weights = [0.717, 0.847, 3.107, 0.420, 0.998]
        zone_fn = zone_private
        x4_label = "X4 = Book Equity / Total Debt"
    else:
        mkcap = args.mkcap if args.mkcap is not None else 0.0
        z, x1, x2, x3, x4, x5 = compute_public(args.wc, args.re, args.ebit, mkcap, args.td, args.rev, args.ta)
        weights = [1.2, 1.4, 3.3, 0.6, 1.0]
        zone_fn = zone_public
        x4_label = "X4 = Market Cap / Total Debt"

    components = [
        ("X1 = Working Capital / Total Assets", x1, weights[0]),
        ("X2 = Retained Earnings / Total Assets", x2, weights[1]),
        ("X3 = EBIT / Total Assets", x3, weights[2]),
        (x4_label, x4, weights[3]),
        ("X5 = Revenue / Total Assets", x5, weights[4]),
    ]

    print(f"  {'Variable':<42} {'Ratio':>8}  {'Weight':>7}  {'Contribution':>12}")
    print("  " + "-" * 74)
    for name, val, wt in components:
        contribution = val * wt
        print(f"  {name:<42} {val:>8.4f}  {wt:>7.3f}  {contribution:>12.4f}")

    zone_label, zone_desc = zone_fn(z)

    print("\n" + "=" * 60)
    print(f"  Z-SCORE:  {z:.4f}   {bar(z, 0, 4)}")
    print(f"  ZONE:     {zone_label}")
    print(f"  VERDICT:  {zone_desc}")
    print("=" * 60)

    if args.private:
        print("\n  THRESHOLDS (Z'-Score for private companies):")
        print("  ─────────────────────────────────────────────")
        print("   Z' > 2.90  →  SAFE ZONE     (low default risk)")
        print("   1.23–2.90  →  GREY ZONE     (moderate risk)")
        print("   Z' < 1.23  →  DISTRESS ZONE (high default risk)")
    else:
        print("\n  THRESHOLDS (Z-Score for public companies):")
        print("  ──────────────────────────────────────────")
        print("   Z  > 2.99  →  SAFE ZONE     (low default risk)")
        print("   1.81–2.99  →  GREY ZONE     (moderate risk)")
        print("   Z  < 1.81  →  DISTRESS ZONE (high default risk)")

    print("\n  NOTE: Altman Z-Score is most predictive for manufacturing firms.")
    print("  Service companies and financial firms may require adjusted models.")
    print("  Always supplement with qualitative credit analysis.\n")


if __name__ == "__main__":
    main()
