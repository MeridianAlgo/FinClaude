#!/usr/bin/env python3
"""
Bond Mathematics Calculator
Computes price, YTM, duration, convexity, DV01, and price sensitivity scenarios.

Usage (price → yield):
  python .claude/tools/bond.py --face 1000 --coupon 0.045 --freq 2 --years 5 --price 98.5

Usage (yield → price):
  python .claude/tools/bond.py --face 1000 --coupon 0.045 --freq 2 --years 5 --ytm 0.048

Add --scenarios to show price sensitivity table.
Add --treasury RATE to compute spread vs. Treasury.
"""

import argparse
import math
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def bond_price(face, coupon_rate, ytm, freq, periods):
    """Compute clean bond price given YTM."""
    c = face * coupon_rate / freq   # periodic coupon payment
    y = ytm / freq                  # periodic yield
    if y == 0:
        return c * periods + face
    pv_coupons = c * (1 - (1 + y) ** (-periods)) / y
    pv_face    = face / (1 + y) ** periods
    return pv_coupons + pv_face


def ytm_solver(face, coupon_rate, freq, periods, price, tol=1e-8, max_iter=1000):
    """Newton-Raphson solver for YTM given price."""
    # Initial guess: approximate YTM
    annual_coupon = face * coupon_rate
    ytm = (annual_coupon + (face - price) / (periods / freq)) / ((face + price) / 2)
    ytm = max(0.0001, ytm)

    for _ in range(max_iter):
        p = bond_price(face, coupon_rate, ytm, freq, periods)
        # Numerical derivative
        delta = ytm * 1e-5 + 1e-8
        dp = (bond_price(face, coupon_rate, ytm + delta, freq, periods) -
              bond_price(face, coupon_rate, ytm - delta, freq, periods)) / (2 * delta)
        if abs(dp) < 1e-12:
            break
        ytm_new = ytm - (p - price) / dp
        ytm_new = max(0.0001, ytm_new)
        if abs(ytm_new - ytm) < tol:
            ytm = ytm_new
            break
        ytm = ytm_new

    return ytm


def macaulay_duration(face, coupon_rate, ytm, freq, periods):
    """Compute Macaulay duration in years."""
    y = ytm / freq
    c = face * coupon_rate / freq
    price = bond_price(face, coupon_rate, ytm, freq, periods)

    weighted = 0.0
    for t in range(1, periods + 1):
        cf = c if t < periods else c + face
        pv = cf / (1 + y) ** t
        weighted += (t / freq) * pv

    return weighted / price


def modified_duration(mac_dur, ytm, freq):
    return mac_dur / (1 + ytm / freq)


def convexity(face, coupon_rate, ytm, freq, periods):
    """Compute convexity."""
    y = ytm / freq
    c = face * coupon_rate / freq
    price = bond_price(face, coupon_rate, ytm, freq, periods)

    conv_sum = 0.0
    for t in range(1, periods + 1):
        cf = c if t < periods else c + face
        pv = cf / (1 + y) ** t
        conv_sum += pv * t * (t + 1)

    return conv_sum / (price * (1 + y) ** 2 * freq ** 2)


def price_change(price, mod_dur, conv, dy):
    """Estimate price change for a given yield shift dy (in decimal)."""
    dur_effect  = -mod_dur * dy * price
    conv_effect = 0.5 * conv * dy ** 2 * price
    return dur_effect + conv_effect


def main():
    parser = argparse.ArgumentParser(
        description="Bond Mathematics Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--face",       type=float, default=1000,  help="Face/par value (default: 1000)")
    parser.add_argument("--coupon",     type=float, required=True, help="Annual coupon rate (e.g. 0.045 for 4.5%%)")
    parser.add_argument("--freq",       type=int,   default=2,     help="Coupon frequency per year (default: 2 = semi-annual)")
    parser.add_argument("--years",      type=float, required=True, help="Years to maturity")
    parser.add_argument("--price",      type=float, default=None,  help="Clean price as %% of par (e.g. 98.5 means $985 per $1000 face)")
    parser.add_argument("--ytm",        type=float, default=None,  help="Yield to maturity (e.g. 0.048 for 4.8%%)")
    parser.add_argument("--treasury",   type=float, default=None,  help="Benchmark Treasury yield for spread calc")
    parser.add_argument("--scenarios",  action="store_true",       help="Print price sensitivity scenarios")
    parser.add_argument("--issuer",     type=str,   default="",    help="Issuer name (optional)")

    args = parser.parse_args()

    if args.price is None and args.ytm is None:
        print("ERROR: Provide either --price or --ytm.", file=sys.stderr)
        sys.exit(1)

    face   = args.face
    cr     = args.coupon
    freq   = args.freq
    years  = args.years
    periods = int(round(years * freq))

    # Actual dollar price
    if args.price is not None:
        price_pct = args.price
        price_dollar = face * price_pct / 100
        ytm = ytm_solver(face, cr, freq, periods, price_dollar)
    else:
        ytm = args.ytm
        price_dollar = bond_price(face, cr, ytm, freq, periods)
        price_pct = price_dollar / face * 100

    annual_coupon = face * cr
    current_yield = annual_coupon / price_dollar

    mac_dur = macaulay_duration(face, cr, ytm, freq, periods)
    mod_dur = modified_duration(mac_dur, ytm, freq)
    conv    = convexity(face, cr, ytm, freq, periods)
    dv01    = mod_dur * price_dollar * 0.0001  # $ change per 1bp

    label = f" — {args.issuer}" if args.issuer else ""

    print("=" * 62)
    print(f"  BOND ANALYSIS{label}")
    print(f"  {cr*100:.3f}% Coupon | {years:.1f}yr Maturity | {freq}x/year")
    print("=" * 62)

    print(f"\n  PRICE & YIELD")
    print(f"  {'─'*48}")
    print(f"  {'Clean Price (% of par)':<36} {price_pct:>8.4f}%")
    print(f"  {'Clean Price ($)':<36} {price_dollar:>9.4f}")
    print(f"  {'Face Value ($)':<36} {face:>9.2f}")
    premium_discount = price_dollar - face
    pd_label = "Premium" if premium_discount > 0 else "Discount"
    print(f"  {pd_label + ' / (Discount)':<36} {premium_discount:>+9.2f}")
    print(f"  {'Annual Coupon ($)':<36} {annual_coupon:>9.2f}")
    print(f"  {'Coupon Rate':<36} {cr*100:>8.3f}%")
    print(f"  {'Current Yield':<36} {current_yield*100:>8.3f}%")
    print(f"  {'Yield to Maturity (YTM)':<36} {ytm*100:>8.4f}%")

    if args.treasury:
        spread_bps = (ytm - args.treasury) * 10000
        print(f"  {'Treasury Benchmark':<36} {args.treasury*100:>8.4f}%")
        print(f"  {'Spread vs. Treasury':<36} {spread_bps:>7.1f} bps")

    print(f"\n  RISK METRICS")
    print(f"  {'─'*48}")
    print(f"  {'Macaulay Duration':<36} {mac_dur:>8.4f} yrs")
    print(f"  {'Modified Duration':<36} {mod_dur:>8.4f}")
    print(f"  {'Convexity':<36} {conv:>8.4f}")
    print(f"  {'DV01 ($ per $1M face, per 1bp)':<36} {dv01 * 1000:>8.2f}")
    print(f"  {'DV01 ($ per bond, per 1bp)':<36} {dv01:>8.4f}")

    # Interpretation: % price change for 100bp move
    p100_dur  = -mod_dur * 0.01 * 100
    p100_full = price_change(price_dollar, mod_dur, conv, 0.01) / price_dollar * 100
    print(f"  {'Price chg for +100bp (duration only)':<36} {p100_dur:>+7.2f}%")
    print(f"  {'Price chg for +100bp (dur+convexity)':<36} {p100_full:>+7.2f}%")

    print(f"\n  CASH FLOW SCHEDULE (first 6 payments + maturity)")
    print(f"  {'─'*52}")
    print(f"  {'Period':<8} {'Year':<8} {'Cash Flow':>12}  {'PV @ YTM':>12}")
    print(f"  {'─'*52}")
    y_per = ytm / freq
    displayed = 0
    for t in range(1, periods + 1):
        cf = annual_coupon / freq
        if t == periods:
            cf += face
        pv = cf / (1 + y_per) ** t
        year = t / freq
        if t <= 6 or t == periods:
            if t == 7 and periods > 7:
                print(f"  {'...':<8} {'...':<8} {'...':>12}  {'...':>12}")
            print(f"  {t:<8} {year:<8.2f} {cf:>12.2f}  {pv:>12.4f}")
            displayed += 1

    if args.scenarios:
        shifts = [-200, -100, -50, -25, -10, +10, +25, +50, +100, +200]
        print(f"\n  PRICE SENSITIVITY SCENARIOS")
        print(f"  {'─'*70}")
        print(f"  {'Yield Change':>14}  {'New YTM':>10}  {'New Price':>12}  {'$ Change':>12}  {'% Change':>10}")
        print(f"  {'─'*70}")
        for shift_bps in shifts:
            shift = shift_bps / 10000
            new_ytm = ytm + shift
            if new_ytm <= 0:
                continue
            new_price = bond_price(face, cr, new_ytm, freq, periods)
            dollar_chg = new_price - price_dollar
            pct_chg    = dollar_chg / price_dollar * 100
            arrow = "▲" if dollar_chg > 0 else "▼"
            print(f"  {f'{shift_bps:+d} bps':>14}  {new_ytm*100:>9.4f}%  {new_price:>12.4f}  {dollar_chg:>+11.4f}  {pct_chg:>+9.3f}% {arrow}")

    print(f"\n  BREAK-EVEN ANALYSIS")
    print(f"  Break-even yield rise = CY / ModDur = {current_yield*100:.3f}% / {mod_dur:.4f} = {current_yield/mod_dur*100:.1f} bps")
    print(f"  (Yield would need to rise >{current_yield/mod_dur*100:.0f}bps for the capital loss to exceed 1yr coupon income)")

    print(f"\n  NOTE: Clean price shown. Add accrued interest for dirty (settlement) price.")
    print(f"  This calculator assumes bullet maturity with no call/put features.\n")


if __name__ == "__main__":
    main()
