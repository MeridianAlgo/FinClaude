#!/usr/bin/env python3
"""
Black-Scholes Options Pricing Calculator
Computes call/put prices, all Greeks, and break-even analysis.

Usage:
  python .claude/tools/black_scholes.py --spot 150 --strike 155 --rate 0.05 --vol 0.25 --tte 0.5 --type call
  python .claude/tools/black_scholes.py --spot 150 --strike 155 --rate 0.05 --vol 0.25 --tte 0.5 --type put --div 0.015
  python .claude/tools/black_scholes.py --spot 150 --strike 155 --rate 0.05 --vol 0.25 --tte 0.5 --both

Add --scenarios to see P&L across a range of spot prices and vols.
Add --iv PRICE to compute implied volatility from market price.
"""

import argparse
import math
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def norm_cdf(x):
    """Standard normal CDF using error function."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_pdf(x):
    """Standard normal PDF."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def d1d2(S, K, r, sigma, T, q=0.0):
    if T <= 0:
        print("ERROR: Time to expiry must be positive.", file=sys.stderr)
        sys.exit(1)
    if sigma <= 0:
        print("ERROR: Volatility must be positive.", file=sys.stderr)
        sys.exit(1)
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return d1, d2


def call_price(S, K, r, sigma, T, q=0.0):
    d1, d2 = d1d2(S, K, r, sigma, T, q)
    return S * math.exp(-q * T) * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)


def put_price(S, K, r, sigma, T, q=0.0):
    d1, d2 = d1d2(S, K, r, sigma, T, q)
    return K * math.exp(-r * T) * norm_cdf(-d2) - S * math.exp(-q * T) * norm_cdf(-d1)


def greeks(S, K, r, sigma, T, q=0.0, opt_type="call"):
    d1, d2 = d1d2(S, K, r, sigma, T, q)
    sqrt_T = math.sqrt(T)
    Nd1  = norm_cdf(d1)
    Nd2  = norm_cdf(d2)
    Nnd1 = norm_cdf(-d1)
    Nnd2 = norm_cdf(-d2)
    npd1 = norm_pdf(d1)

    # Delta
    if opt_type == "call":
        delta = math.exp(-q * T) * Nd1
    else:
        delta = math.exp(-q * T) * (Nd1 - 1)

    # Gamma (same for call and put)
    gamma = math.exp(-q * T) * npd1 / (S * sigma * sqrt_T)

    # Theta (per calendar day)
    if opt_type == "call":
        theta = (-(S * math.exp(-q * T) * npd1 * sigma / (2 * sqrt_T))
                 - r * K * math.exp(-r * T) * Nd2
                 + q * S * math.exp(-q * T) * Nd1) / 365
    else:
        theta = (-(S * math.exp(-q * T) * npd1 * sigma / (2 * sqrt_T))
                 + r * K * math.exp(-r * T) * Nnd2
                 - q * S * math.exp(-q * T) * Nnd1) / 365

    # Vega (per 1% change in vol)
    vega = S * math.exp(-q * T) * npd1 * sqrt_T / 100

    # Rho (per 1% change in rate)
    if opt_type == "call":
        rho = K * T * math.exp(-r * T) * Nd2 / 100
    else:
        rho = -K * T * math.exp(-r * T) * Nnd2 / 100

    # Vanna (dDelta/dVol) — useful for vol surface trading
    vanna = -math.exp(-q * T) * npd1 * d2 / sigma

    # Charm (dDelta/dT — delta decay per day)
    if opt_type == "call":
        charm = math.exp(-q * T) * (npd1 * (2 * (r - q) * T - d2 * sigma * sqrt_T) /
                                    (2 * T * sigma * sqrt_T) - q * Nd1) / 365
    else:
        charm = math.exp(-q * T) * (npd1 * (2 * (r - q) * T - d2 * sigma * sqrt_T) /
                                    (2 * T * sigma * sqrt_T) + q * Nnd1) / 365

    return {
        "delta": delta, "gamma": gamma, "theta": theta,
        "vega": vega, "rho": rho, "vanna": vanna, "charm": charm
    }


def implied_vol(S, K, r, T, q, market_price, opt_type, tol=1e-6, max_iter=500):
    """Newton-Raphson IV solver."""
    # Initial guess using Brenner-Subrahmanyam approximation
    sigma = math.sqrt(2 * math.pi / T) * market_price / S
    sigma = max(0.001, min(sigma, 5.0))

    price_fn = call_price if opt_type == "call" else put_price

    for _ in range(max_iter):
        price = price_fn(S, K, r, sigma, T, q)
        d1, _ = d1d2(S, K, r, sigma, T, q)
        vega = S * math.exp(-q * T) * norm_pdf(d1) * math.sqrt(T)
        if abs(vega) < 1e-12:
            break
        sigma_new = sigma - (price - market_price) / vega
        sigma_new = max(0.001, min(sigma_new, 5.0))
        if abs(sigma_new - sigma) < tol:
            return sigma_new
        sigma = sigma_new

    return sigma


def moneyness(S, K):
    pct = (S - K) / K * 100
    if abs(pct) < 2:
        return f"ATM ({pct:+.1f}%)"
    elif pct > 0:
        return f"ITM ({pct:+.1f}%)"
    else:
        return f"OTM ({pct:+.1f}%)"


def print_option(S, K, r, sigma, T, q, opt_type):
    price_fn = call_price if opt_type == "call" else put_price
    price = price_fn(S, K, r, sigma, T, q)
    g = greeks(S, K, r, sigma, T, q, opt_type)

    label = opt_type.upper()
    d1, d2 = d1d2(S, K, r, sigma, T, q)
    intrinsic = max(0, S - K) if opt_type == "call" else max(0, K - S)
    time_val  = price - intrinsic

    print(f"\n  {label} OPTION")
    print(f"  {'─'*50}")
    print(f"  {'Option Price':<34} ${price:>9.4f}")
    print(f"  {'Intrinsic Value':<34} ${intrinsic:>9.4f}")
    print(f"  {'Time Value':<34} ${time_val:>9.4f}")
    print(f"  {'Time Value %':<34}  {time_val/price*100 if price>0 else 0:>8.1f}%")
    print(f"  {'Moneyness':<34}  {moneyness(S, K)}")
    print(f"  {'d1':<34}  {d1:>9.4f}")
    print(f"  {'d2':<34}  {d2:>9.4f}")
    print(f"  {'N(d1)':<34}  {norm_cdf(d1):>9.4f}")
    print(f"  {'N(d2)':<34}  {norm_cdf(d2):>9.4f}")

    print(f"\n  GREEKS")
    print(f"  {'─'*50}")
    print(f"  {'Delta  (price chg per $1 spot move)':<34}  {g['delta']:>+9.4f}")
    print(f"  {'Gamma  (delta chg per $1 spot move)':<34}  {g['gamma']:>+9.4f}")
    print(f"  {'Theta  (price decay per calendar day)':<34} ${g['theta']:>+9.4f}")
    print(f"  {'Vega   (price chg per 1% vol move)':<34} ${g['vega']:>+9.4f}")
    print(f"  {'Rho    (price chg per 1% rate move)':<34} ${g['rho']:>+9.4f}")
    print(f"  {'Vanna  (dDelta/dVol)':<34}  {g['vanna']:>+9.4f}")
    print(f"  {'Charm  (dDelta/day)':<34}  {g['charm']:>+9.6f}")

    # Practical interpretations
    days_to_exp = T * 365
    print(f"\n  PRACTICAL INTERPRETATION")
    print(f"  {'─'*50}")
    print(f"  Per $1 spot move:        option changes ${g['delta']:.4f} (Delta)")
    print(f"  Per 1% spot move:        option changes ${g['delta']*S*0.01:.4f}")
    print(f"  Daily time decay:        option loses  ${abs(g['theta']):.4f}/day")
    print(f"  Per 1% vol increase:     option gains  ${g['vega']:.4f}")
    print(f"  Days to expiry:          {days_to_exp:.0f} days")
    print(f"  Total remaining theta:  ${abs(g['theta']) * days_to_exp:.2f} (theta × days)")

    # Break-evens
    if opt_type == "call":
        be = K + price
        print(f"  Break-even at expiry:   ${be:.4f} (stock must be above this)")
    else:
        be = K - price
        print(f"  Break-even at expiry:   ${be:.4f} (stock must be below this)")

    return price, g


def scenarios_table(S, K, r, T, q, opt_type):
    spot_range  = [S * x for x in [0.80, 0.85, 0.90, 0.95, 1.0, 1.05, 1.10, 1.15, 1.20]]
    sigma_range = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]

    # Get base price at current vol
    price_fn = call_price if opt_type == "call" else put_price

    print(f"\n  P&L SCENARIOS (spot vs. implied vol)")
    print(f"  Base vol shown in header | Rows = Spot Price | Columns = IV\n")

    header = f"  {'Spot':>8}"
    for sig in sigma_range:
        header += f"  {'IV '+str(int(sig*100))+'%':>9}"
    print(header)
    print("  " + "─" * (8 + len(sigma_range) * 11 + 4))

    for spot in spot_range:
        row = f"  {spot:>8.2f}"
        for sig in sigma_range:
            try:
                p = price_fn(spot, K, r, sig, T, q)
                row += f"  {p:>9.4f}"
            except Exception:
                row += f"  {'N/A':>9}"
        marker = " ◄" if abs(spot - S) < 0.01 else ""
        print(row + marker)
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Black-Scholes Options Pricing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--spot",   type=float, required=True, help="Current stock/spot price")
    parser.add_argument("--strike", type=float, required=True, help="Strike price")
    parser.add_argument("--rate",   type=float, required=True, help="Risk-free rate (e.g. 0.05 for 5%%)")
    parser.add_argument("--vol",    type=float, default=None,  help="Implied volatility (e.g. 0.25 for 25%%)")
    parser.add_argument("--tte",    type=float, required=True, help="Time to expiry in years (e.g. 0.5 = 6 months)")
    parser.add_argument("--type",   type=str,   default="both", choices=["call","put","both"], help="Option type")
    parser.add_argument("--div",    type=float, default=0.0,  help="Continuous dividend yield (e.g. 0.015 for 1.5%%)")
    parser.add_argument("--iv",     type=float, default=None, help="Market option price → compute implied vol")
    parser.add_argument("--scenarios", action="store_true",   help="Print P&L scenario matrix")
    parser.add_argument("--ticker",    type=str, default="",  help="Ticker symbol (optional)")

    args = parser.parse_args()

    S = args.spot
    K = args.strike
    r = args.rate
    T = args.tte
    q = args.div

    label = f" — {args.ticker}" if args.ticker else ""

    print("=" * 62)
    print(f"  BLACK-SCHOLES OPTIONS ANALYSIS{label}")
    print(f"  Spot: ${S:.2f}  |  Strike: ${K:.2f}  |  TTE: {T*365:.0f}d ({T:.4f}yr)")
    print(f"  Risk-Free: {r*100:.2f}%  |  Div Yield: {q*100:.2f}%  |  Moneyness: {moneyness(S,K)}")
    print("=" * 62)

    if args.iv is not None:
        # Compute implied vol
        opt_type_iv = "call" if args.type == "both" else args.type
        iv = implied_vol(S, K, r, T, q, args.iv, opt_type_iv)
        print(f"\n  IMPLIED VOLATILITY SOLVER")
        print(f"  Market Price ({opt_type_iv}):  ${args.iv:.4f}")
        print(f"  Implied Volatility:    {iv*100:.4f}%")
        print(f"  Annualized 1-sigma move: ±${S*iv:.2f} ({iv*100:.1f}%)")
        sigma = iv
    elif args.vol is not None:
        sigma = args.vol
    else:
        print("ERROR: Provide either --vol or --iv.", file=sys.stderr)
        sys.exit(1)

    print(f"\n  Volatility: {sigma*100:.2f}%  |  1-sigma annual move: ±${S*sigma:.2f}")
    print(f"  1-sigma daily move: ±${S*sigma/math.sqrt(252):.2f}")

    if args.type in ("call", "both"):
        print_option(S, K, r, sigma, T, q, "call")

    if args.type in ("put", "both"):
        print_option(S, K, r, sigma, T, q, "put")

    if args.type == "both":
        c = call_price(S, K, r, sigma, T, q)
        p = put_price(S, K, r, sigma, T, q)
        parity_diff = c - p - (S * math.exp(-q * T) - K * math.exp(-r * T))
        print(f"\n  PUT-CALL PARITY CHECK")
        print(f"  {'─'*48}")
        print(f"  Call: ${c:.4f}  |  Put: ${p:.4f}")
        print(f"  C - P - (S·e^(-qT) - K·e^(-rT)) = {parity_diff:.6f}  {'✓ OK' if abs(parity_diff) < 0.001 else '⚠ Check inputs'}")

    if args.scenarios and sigma is not None:
        scenarios_table(S, K, r, T, q, args.type if args.type != "both" else "call")

    print(f"\n  ASSUMPTIONS: European-style, no early exercise, lognormal returns.")
    print(f"  Black-Scholes underprices tails (fat tails / vol skew not captured).")
    print(f"  This output is for analytical reference only — not investment advice.\n")


if __name__ == "__main__":
    main()
