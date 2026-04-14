#!/usr/bin/env python3
"""
Portfolio Statistics Calculator
Computes risk/return metrics: Sharpe, Sortino, VaR, CVaR, max drawdown, and more.

Usage (single asset returns):
  python .claude/tools/portfolio.py --returns "0.01,-0.02,0.03,0.01,-0.01,0.02,0.04,-0.01,0.02" --rf 0.05

Usage (multiple assets with weights):
  python .claude/tools/portfolio.py \
    --assets "AAPL,MSFT,NVDA" \
    --weights "0.4,0.35,0.25" \
    --returns-a "0.01,-0.02,0.03,0.01,-0.01,0.02" \
    --returns-b "0.015,-0.01,0.025,0.005,-0.005,0.018" \
    --returns-c "-0.01,0.04,0.06,-0.02,0.02,0.03" \
    --rf 0.05

Returns should be decimal daily/weekly/monthly returns (e.g. 0.01 = +1%).
Use --freq to specify (daily=252, weekly=52, monthly=12).
"""

import argparse
import math
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def mean(data):
    return sum(data) / len(data) if data else 0.0


def variance(data, ddof=1):
    m = mean(data)
    n = len(data)
    if n <= ddof:
        return 0.0
    return sum((x - m) ** 2 for x in data) / (n - ddof)


def stdev(data, ddof=1):
    return math.sqrt(variance(data, ddof))


def covariance(a, b, ddof=1):
    if len(a) != len(b) or len(a) <= ddof:
        return 0.0
    ma, mb = mean(a), mean(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (len(a) - ddof)


def correlation(a, b):
    sa, sb = stdev(a), stdev(b)
    if sa == 0 or sb == 0:
        return 0.0
    return covariance(a, b) / (sa * sb)


def annualized_return(returns, freq):
    """Compound annual return."""
    total = 1.0
    for r in returns:
        total *= (1 + r)
    periods = len(returns)
    return total ** (freq / periods) - 1


def annualized_vol(returns, freq):
    return stdev(returns) * math.sqrt(freq)


def sharpe_ratio(returns, rf_annual, freq):
    ret = annualized_return(returns, freq)
    vol = annualized_vol(returns, freq)
    if vol == 0:
        return 0.0
    return (ret - rf_annual) / vol


def sortino_ratio(returns, rf_annual, freq):
    ret = annualized_return(returns, freq)
    rf_periodic = (1 + rf_annual) ** (1 / freq) - 1
    downside = [r for r in returns if r < rf_periodic]
    if not downside:
        return float("inf")
    downside_vol = math.sqrt(sum((r - rf_periodic) ** 2 for r in downside) / len(returns)) * math.sqrt(freq)
    if downside_vol == 0:
        return 0.0
    return (ret - rf_annual) / downside_vol


def max_drawdown(returns):
    """Max drawdown from peak to trough."""
    peak = 1.0
    portfolio = 1.0
    max_dd = 0.0
    peak_idx = 0
    trough_idx = 0
    cur_peak_idx = 0

    cum = [1.0]
    for r in returns:
        cum.append(cum[-1] * (1 + r))

    peak_val = cum[0]
    for i, v in enumerate(cum):
        if v > peak_val:
            peak_val = v
            cur_peak_idx = i
        dd = (v - peak_val) / peak_val
        if dd < max_dd:
            max_dd = dd
            peak_idx = cur_peak_idx
            trough_idx = i

    return max_dd, peak_idx, trough_idx


def var(returns, confidence=0.95):
    """Historical Value at Risk."""
    sorted_r = sorted(returns)
    idx = int((1 - confidence) * len(sorted_r))
    return sorted_r[max(0, idx)]


def cvar(returns, confidence=0.95):
    """Conditional VaR / Expected Shortfall."""
    var_val = var(returns, confidence)
    tail = [r for r in returns if r <= var_val]
    return mean(tail) if tail else var_val


def skewness(data):
    m = mean(data)
    n = len(data)
    s = stdev(data)
    if s == 0 or n < 3:
        return 0.0
    return sum((x - m) ** 3 for x in data) / n / (s ** 3)


def kurtosis(data):
    """Excess kurtosis (normal = 0)."""
    m = mean(data)
    n = len(data)
    s = stdev(data)
    if s == 0 or n < 4:
        return 0.0
    return sum((x - m) ** 4 for x in data) / n / (s ** 4) - 3


def calmar_ratio(returns, freq):
    ann_ret = annualized_return(returns, freq)
    max_dd_val, _, _ = max_drawdown(returns)
    if max_dd_val == 0:
        return float("inf")
    return ann_ret / abs(max_dd_val)


def print_stats(name, returns, rf_annual, freq):
    n = len(returns)
    ann_ret = annualized_return(returns, freq)
    ann_vol = annualized_vol(returns, freq)
    sharpe  = sharpe_ratio(returns, rf_annual, freq)
    sortino = sortino_ratio(returns, rf_annual, freq)
    max_dd, pi, ti = max_drawdown(returns)
    var_95  = var(returns, 0.95)
    var_99  = var(returns, 0.99)
    cvar_95 = cvar(returns, 0.95)
    calmar  = calmar_ratio(returns, freq)
    skew    = skewness(returns)
    kurt    = kurtosis(returns)

    pos  = sum(1 for r in returns if r > 0)
    neg  = sum(1 for r in returns if r < 0)
    hit_rate = pos / n * 100 if n > 0 else 0

    best  = max(returns)
    worst = min(returns)
    avg   = mean(returns)

    freq_label = {252: "daily", 52: "weekly", 12: "monthly", 4: "quarterly", 1: "annual"}.get(freq, str(freq))

    print(f"\n  {'─'*58}")
    print(f"  PORTFOLIO: {name.upper()}")
    print(f"  {n} {freq_label} observations  |  Annualization factor: {freq}")
    print(f"  {'─'*58}")

    print(f"\n  RETURN METRICS")
    print(f"  {'─'*50}")
    print(f"  {'Annualized Return':<36} {ann_ret*100:>+8.2f}%")
    print(f"  {'Annualized Volatility':<36} {ann_vol*100:>8.2f}%")
    print(f"  {'Period Mean Return':<36} {avg*100:>+8.4f}%")
    print(f"  {'Best Period':<36} {best*100:>+8.2f}%")
    print(f"  {'Worst Period':<36} {worst*100:>+8.2f}%")
    print(f"  {'Hit Rate (positive periods)':<36} {hit_rate:>8.1f}%  ({pos} up / {neg} down)")

    print(f"\n  RISK-ADJUSTED METRICS")
    print(f"  {'─'*50}")
    print(f"  {'Sharpe Ratio':<36} {sharpe:>8.3f}  {'✓ Good' if sharpe>1 else ('⚠ Marginal' if sharpe>0.5 else '✗ Weak')}")
    print(f"  {'Sortino Ratio':<36} {sortino:>8.3f}  (penalizes downside only)")
    print(f"  {'Calmar Ratio':<36} {calmar:>8.3f}  (return / max drawdown)")

    print(f"\n  RISK METRICS")
    print(f"  {'─'*50}")
    print(f"  {'Max Drawdown':<36} {max_dd*100:>+8.2f}%")
    print(f"  {'VaR (95%, 1-period)':<36} {var_95*100:>+8.2f}%")
    print(f"  {'VaR (99%, 1-period)':<36} {var_99*100:>+8.2f}%")
    print(f"  {'CVaR / ES (95%)':<36} {cvar_95*100:>+8.2f}%  (avg loss beyond VaR)")

    print(f"\n  DISTRIBUTION SHAPE")
    print(f"  {'─'*50}")
    print(f"  {'Skewness':<36} {skew:>8.4f}  {'positive tail' if skew>0.5 else ('negative tail' if skew<-0.5 else 'near-symmetric')}")
    print(f"  {'Excess Kurtosis':<36} {kurt:>8.4f}  {'fat tails' if kurt>1 else ('thin tails' if kurt<-1 else 'near-normal')}")

    return ann_ret, ann_vol, sharpe


def portfolio_weights_stats(asset_names, weights, all_returns, rf_annual, freq):
    """Compute combined portfolio stats given weights and per-asset returns."""
    n_assets = len(weights)
    n_periods = len(all_returns[0])

    # Portfolio return series
    port_returns = []
    for t in range(n_periods):
        pr = sum(weights[i] * all_returns[i][t] for i in range(n_assets))
        port_returns.append(pr)

    print(f"\n  ASSET CORRELATION MATRIX")
    print(f"  {'─'*60}")
    header = f"  {'':>10}"
    for name in asset_names:
        header += f"  {name:>10}"
    print(header)
    for i, ai in enumerate(asset_names):
        row = f"  {ai:>10}"
        for j, _ in enumerate(asset_names):
            c = correlation(all_returns[i], all_returns[j])
            row += f"  {c:>10.4f}"
        print(row)

    print(f"\n  PER-ASSET STATISTICS")
    stats_list = []
    for i, name in enumerate(asset_names):
        ann_r, ann_v, sharpe = print_stats(name, all_returns[i], rf_annual, freq)
        stats_list.append((name, weights[i], ann_r, ann_v, sharpe))

    print(f"\n{'='*60}")
    print(f"  COMBINED PORTFOLIO WEIGHTS SUMMARY")
    print(f"  {'─'*58}")
    print(f"  {'Asset':<12} {'Weight':>8}  {'Ann.Ret':>10}  {'Ann.Vol':>10}  {'Sharpe':>8}  {'Contribution'}")
    print(f"  {'─'*58}")
    for name, w, r, v, s in stats_list:
        contrib = w * r * 100
        print(f"  {name:<12} {w*100:>7.1f}%  {r*100:>+9.2f}%  {v*100:>9.2f}%  {s:>8.3f}  {contrib:>+8.2f}%")

    print_stats("COMBINED PORTFOLIO", port_returns, rf_annual, freq)


def main():
    parser = argparse.ArgumentParser(
        description="Portfolio Statistics Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--returns",   type=str, default=None, help="Comma-separated return series")
    parser.add_argument("--assets",    type=str, default=None, help="Comma-separated asset names")
    parser.add_argument("--weights",   type=str, default=None, help="Comma-separated weights (must sum to 1)")
    parser.add_argument("--returns-a", type=str, default=None, help="Returns for asset A")
    parser.add_argument("--returns-b", type=str, default=None, help="Returns for asset B")
    parser.add_argument("--returns-c", type=str, default=None, help="Returns for asset C")
    parser.add_argument("--returns-d", type=str, default=None, help="Returns for asset D")
    parser.add_argument("--rf",   type=float, default=0.05, help="Annual risk-free rate (default: 0.05)")
    parser.add_argument("--freq", type=int,   default=252,  help="Periods per year: 252=daily,52=weekly,12=monthly")
    parser.add_argument("--name", type=str,   default="Portfolio", help="Portfolio name")

    args = parser.parse_args()

    print("=" * 60)
    print(f"  PORTFOLIO STATISTICS — {args.name.upper()}")
    print(f"  Risk-Free Rate: {args.rf*100:.2f}%  |  Freq: {args.freq} periods/year")
    print("=" * 60)

    # Multi-asset mode
    if args.returns_a and args.assets and args.weights:
        asset_names = [x.strip() for x in args.assets.split(",")]
        weights = [float(x.strip()) for x in args.weights.split(",")]
        raw = [args.returns_a, args.returns_b, args.returns_c, args.returns_d]
        all_returns = []
        for r_str in raw:
            if r_str:
                all_returns.append([float(x.strip()) for x in r_str.split(",")])
        if abs(sum(weights) - 1.0) > 0.01:
            print(f"  WARNING: Weights sum to {sum(weights):.4f} (not 1.0) — normalizing.", file=sys.stderr)
            total = sum(weights)
            weights = [w / total for w in weights]
        portfolio_weights_stats(asset_names[:len(all_returns)], weights[:len(all_returns)], all_returns, args.rf, args.freq)
    elif args.returns:
        returns = [float(x.strip()) for x in args.returns.split(",")]
        print_stats(args.name, returns, args.rf, args.freq)
    else:
        print("ERROR: Provide --returns for single-asset or --returns-a/--assets/--weights for multi-asset.", file=sys.stderr)
        sys.exit(1)

    print(f"\n  NOTE: Historical returns do not predict future performance.")
    print(f"  VaR/CVaR are historical — actual tail risk may differ.")
    print(f"  Sharpe > 1.0 generally considered good; > 2.0 excellent.\n")


if __name__ == "__main__":
    main()
