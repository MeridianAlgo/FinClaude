#!/usr/bin/env python3
"""
Technical Indicators Calculator
Computes RSI, MACD, Bollinger Bands, ATR, Stochastic, EMA/SMA, VWAP, and signals.

Usage:
  python .claude/tools/technicals.py --prices "150,152,148,155,153,157,160,158,162,165,163"
  python .claude/tools/technicals.py --prices "..." --highs "..." --lows "..." --volumes "..."
  python .claude/tools/technicals.py --file prices.csv   (CSV: date,close or date,open,high,low,close,volume)

Prices should be ordered oldest → newest (left to right).
"""

import argparse
import math
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


# ─── Core Indicator Functions ────────────────────────────────────────────────

def sma(prices, period):
    if len(prices) < period:
        return [None] * len(prices)
    result = [None] * (period - 1)
    for i in range(period - 1, len(prices)):
        result.append(sum(prices[i - period + 1:i + 1]) / period)
    return result


def ema(prices, period):
    if len(prices) < period:
        return [None] * len(prices)
    result = [None] * (period - 1)
    k = 2.0 / (period + 1)
    # Seed with SMA
    seed = sum(prices[:period]) / period
    ema_val = seed
    result.append(ema_val)
    for price in prices[period:]:
        ema_val = price * k + ema_val * (1 - k)
        result.append(ema_val)
    return result


def rsi(prices, period=14):
    if len(prices) < period + 1:
        return [None] * len(prices)
    result = [None] * period
    gains = []
    losses = []
    for i in range(1, period + 1):
        chg = prices[i] - prices[i - 1]
        gains.append(max(chg, 0))
        losses.append(max(-chg, 0))
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    for i in range(period, len(prices)):
        if i > period:
            chg = prices[i] - prices[i - 1]
            avg_gain = (avg_gain * (period - 1) + max(chg, 0)) / period
            avg_loss = (avg_loss * (period - 1) + max(-chg, 0)) / period
        if avg_loss == 0:
            result.append(100.0)
        else:
            rs = avg_gain / avg_loss
            result.append(100 - 100 / (1 + rs))
    return result


def macd(prices, fast=12, slow=26, signal=9):
    ema_fast = ema(prices, fast)
    ema_slow = ema(prices, slow)
    macd_line = [
        (f - s) if (f is not None and s is not None) else None
        for f, s in zip(ema_fast, ema_slow)
    ]
    # Signal line: EMA of MACD line (non-None values only)
    valid_idx = [i for i, v in enumerate(macd_line) if v is not None]
    if len(valid_idx) < signal:
        return macd_line, [None] * len(prices), [None] * len(prices)
    signal_line = [None] * len(prices)
    valid_macd = [macd_line[i] for i in valid_idx]
    valid_signal = ema(valid_macd, signal)
    for j, i in enumerate(valid_idx):
        signal_line[i] = valid_signal[j]
    histogram = [
        (m - s) if (m is not None and s is not None) else None
        for m, s in zip(macd_line, signal_line)
    ]
    return macd_line, signal_line, histogram


def bollinger_bands(prices, period=20, std_dev=2.0):
    mid = sma(prices, period)
    upper = [None] * len(prices)
    lower = [None] * len(prices)
    bwidth = [None] * len(prices)
    pct_b  = [None] * len(prices)
    for i in range(period - 1, len(prices)):
        window = prices[i - period + 1:i + 1]
        mean = sum(window) / period
        variance = sum((x - mean) ** 2 for x in window) / period
        std = math.sqrt(variance)
        u = mean + std_dev * std
        l = mean - std_dev * std
        upper[i] = u
        lower[i] = l
        bwidth[i] = (u - l) / mean * 100 if mean != 0 else 0
        pct_b[i]  = (prices[i] - l) / (u - l) if (u - l) != 0 else 0.5
    return mid, upper, lower, bwidth, pct_b


def atr(highs, lows, closes, period=14):
    """Average True Range."""
    if len(closes) < 2:
        return [None] * len(closes)
    true_ranges = [highs[0] - lows[0]]  # First bar
    for i in range(1, len(closes)):
        tr = max(
            highs[i] - lows[i],
            abs(highs[i] - closes[i - 1]),
            abs(lows[i] - closes[i - 1])
        )
        true_ranges.append(tr)
    result = [None] * (period - 1)
    seed = sum(true_ranges[:period]) / period
    atr_val = seed
    result.append(atr_val)
    for tr in true_ranges[period:]:
        atr_val = (atr_val * (period - 1) + tr) / period
        result.append(atr_val)
    return result


def stochastic(highs, lows, closes, k_period=14, d_period=3):
    """Stochastic Oscillator %K and %D."""
    pct_k = [None] * len(closes)
    for i in range(k_period - 1, len(closes)):
        highest = max(highs[i - k_period + 1:i + 1])
        lowest  = min(lows[i - k_period + 1:i + 1])
        if highest == lowest:
            pct_k[i] = 50.0
        else:
            pct_k[i] = (closes[i] - lowest) / (highest - lowest) * 100
    pct_d = sma([v if v is not None else 0 for v in pct_k], d_period)
    # Re-apply None mask
    for i in range(min(k_period - 1 + d_period - 1, len(closes))):
        pct_d[i] = None
    return pct_k, pct_d


def vwap(prices, volumes):
    """Volume-weighted average price."""
    if len(prices) != len(volumes):
        return [None] * len(prices)
    total_pv = 0.0
    total_v  = 0.0
    result = []
    for p, v in zip(prices, volumes):
        total_pv += p * v
        total_v  += v
        result.append(total_pv / total_v if total_v > 0 else p)
    return result


def last(series):
    """Return the last non-None value in a series."""
    for v in reversed(series):
        if v is not None:
            return v
    return None


def signal_summary(closes, highs, lows, volumes=None):
    """Generate a signal summary table."""
    price = closes[-1]
    signals = []

    # ─ RSI ─
    rsi_vals = rsi(closes, 14)
    rsi_now  = last(rsi_vals)
    if rsi_now is not None:
        if rsi_now > 70:
            signals.append(("RSI(14)", f"{rsi_now:.1f}", "SELL", "Overbought (>70)"))
        elif rsi_now < 30:
            signals.append(("RSI(14)", f"{rsi_now:.1f}", "BUY", "Oversold (<30)"))
        elif rsi_now > 60:
            signals.append(("RSI(14)", f"{rsi_now:.1f}", "NEUTRAL+", "Mildly bullish (60–70)"))
        elif rsi_now < 40:
            signals.append(("RSI(14)", f"{rsi_now:.1f}", "NEUTRAL-", "Mildly bearish (30–40)"))
        else:
            signals.append(("RSI(14)", f"{rsi_now:.1f}", "NEUTRAL", "No clear signal (40–60)"))

    # ─ MACD ─
    macd_l, sig_l, hist = macd(closes)
    macd_now = last(macd_l)
    sig_now  = last(sig_l)
    hist_now = last(hist)
    if hist_now is not None:
        if hist_now > 0:
            signals.append(("MACD", f"hist={hist_now:.3f}", "BUY", "MACD above signal line"))
        else:
            signals.append(("MACD", f"hist={hist_now:.3f}", "SELL", "MACD below signal line"))

    # ─ Bollinger Bands ─
    mid_bb, upper_bb, lower_bb, bw, pb = bollinger_bands(closes, 20)
    pb_now  = last(pb)
    bw_now  = last(bw)
    if pb_now is not None:
        if pb_now > 1.0:
            signals.append(("Bollinger %B", f"{pb_now:.3f}", "SELL", "Price above upper band"))
        elif pb_now < 0.0:
            signals.append(("Bollinger %B", f"{pb_now:.3f}", "BUY", "Price below lower band"))
        elif pb_now > 0.8:
            signals.append(("Bollinger %B", f"{pb_now:.3f}", "SELL", "Near upper band (>80%)"))
        elif pb_now < 0.2:
            signals.append(("Bollinger %B", f"{pb_now:.3f}", "BUY", "Near lower band (<20%)"))
        else:
            signals.append(("Bollinger %B", f"{pb_now:.3f}", "NEUTRAL", "Mid-band range"))

    # ─ Moving Averages ─
    sma20 = last(sma(closes, 20))
    sma50 = last(sma(closes, 50)) if len(closes) >= 50 else None
    ema12 = last(ema(closes, 12))

    if sma20 is not None:
        rel = (price - sma20) / sma20 * 100
        sig = "BUY" if price > sma20 else "SELL"
        signals.append(("SMA(20)", f"${sma20:.2f}", sig, f"Price {rel:+.1f}% vs 20-day SMA"))

    if sma50 is not None:
        rel = (price - sma50) / sma50 * 100
        sig = "BUY" if price > sma50 else "SELL"
        signals.append(("SMA(50)", f"${sma50:.2f}", sig, f"Price {rel:+.1f}% vs 50-day SMA"))

    if sma20 is not None and sma50 is not None:
        cross = "GOLDEN CROSS (BUY)" if sma20 > sma50 else "DEATH CROSS (SELL)"
        signals.append(("MA Cross", f"20>{50}" if sma20>sma50 else f"20<{50}", "BUY" if sma20>sma50 else "SELL", cross))

    # ─ Stochastic ─
    if len(highs) > 0 and len(lows) > 0:
        k_vals, d_vals = stochastic(highs, lows, closes)
        k_now = last(k_vals)
        d_now = last(d_vals)
        if k_now is not None:
            if k_now > 80:
                signals.append(("Stoch %K", f"{k_now:.1f}", "SELL", "Overbought (>80)"))
            elif k_now < 20:
                signals.append(("Stoch %K", f"{k_now:.1f}", "BUY", "Oversold (<20)"))
            else:
                signals.append(("Stoch %K", f"{k_now:.1f}", "NEUTRAL", "Neutral zone (20–80)"))

    # ─ ATR ─
    if len(highs) > 0 and len(lows) > 0:
        atr_vals = atr(highs, lows, closes)
        atr_now = last(atr_vals)
        if atr_now is not None:
            atr_pct = atr_now / price * 100
            signals.append(("ATR(14)", f"${atr_now:.2f}", "INFO", f"{atr_pct:.2f}% of price — daily volatility gauge"))

    return signals, rsi_now, macd_now, sig_now, hist_now, sma20, sma50, ema12, last(mid_bb), last(upper_bb), last(lower_bb), last(pb), last(bw)


def count_bullish(signals):
    return sum(1 for s in signals if s[2] in ("BUY",))


def count_bearish(signals):
    return sum(1 for s in signals if s[2] in ("SELL",))


def main():
    parser = argparse.ArgumentParser(
        description="Technical Indicators Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--prices",  type=str, default=None, help="Comma-separated close prices (oldest first)")
    parser.add_argument("--highs",   type=str, default=None, help="Comma-separated high prices")
    parser.add_argument("--lows",    type=str, default=None, help="Comma-separated low prices")
    parser.add_argument("--volumes", type=str, default=None, help="Comma-separated volumes")
    parser.add_argument("--file",    type=str, default=None, help="CSV file: date,close or date,open,high,low,close,volume")
    parser.add_argument("--ticker",  type=str, default="",   help="Ticker symbol for display")
    parser.add_argument("--period",  type=str, default="daily", help="Period label (daily/weekly/monthly)")

    args = parser.parse_args()

    # Load data
    closes = highs = lows = volumes = []

    if args.file:
        rows = []
        with open(args.file) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or line.lower().startswith('date'):
                    continue
                parts = line.split(',')
                rows.append([p.strip() for p in parts])
        if len(rows[0]) >= 6:
            closes  = [float(r[4]) for r in rows]
            highs   = [float(r[2]) for r in rows]
            lows    = [float(r[3]) for r in rows]
            volumes = [float(r[5]) for r in rows]
        elif len(rows[0]) == 2:
            closes = [float(r[1]) for r in rows]
        else:
            closes = [float(r[-1]) for r in rows]
    elif args.prices:
        closes = [float(x.strip()) for x in args.prices.split(',') if x.strip()]
        if args.highs:
            highs  = [float(x.strip()) for x in args.highs.split(',') if x.strip()]
        if args.lows:
            lows   = [float(x.strip()) for x in args.lows.split(',') if x.strip()]
        if args.volumes:
            volumes = [float(x.strip()) for x in args.volumes.split(',') if x.strip()]
    else:
        print("ERROR: Provide --prices or --file.", file=sys.stderr)
        sys.exit(1)

    if not highs:
        highs = closes
    if not lows:
        lows = closes

    n = len(closes)
    price = closes[-1]
    label = f" — {args.ticker}" if args.ticker else ""

    print("=" * 64)
    print(f"  TECHNICAL ANALYSIS{label}")
    print(f"  {n} {args.period} bars  |  Latest Close: ${price:.2f}")
    print("=" * 64)

    # Price context
    highest = max(closes)
    lowest  = min(closes)
    pct_from_high = (price - highest) / highest * 100
    pct_from_low  = (price - lowest)  / lowest  * 100
    print(f"\n  PRICE CONTEXT")
    print(f"  {'─'*52}")
    print(f"  {'Current Price':<28} ${price:.2f}")
    print(f"  {'Period High':<28} ${highest:.2f}  ({pct_from_high:+.1f}% from high)")
    print(f"  {'Period Low':<28} ${lowest:.2f}  ({pct_from_low:+.1f}% from low)")
    if n >= 2:
        chg = (closes[-1] - closes[-2]) / closes[-2] * 100
        print(f"  {'Last Bar Change':<28} {chg:+.2f}%")
    if n >= 5:
        wk = (closes[-1] - closes[-5]) / closes[-5] * 100
        print(f"  {'5-Bar Return':<28} {wk:+.2f}%")
    if n >= 20:
        mo = (closes[-1] - closes[-20]) / closes[-20] * 100
        print(f"  {'20-Bar Return':<28} {mo:+.2f}%")

    (signals, rsi_now, macd_now, sig_now, hist_now,
     sma20, sma50, ema12, bb_mid, bb_upper, bb_lower, pb, bw) = signal_summary(closes, highs, lows, volumes if volumes else None)

    print(f"\n  KEY INDICATOR VALUES")
    print(f"  {'─'*52}")
    if rsi_now  is not None: print(f"  {'RSI(14)':<28} {rsi_now:.2f}")
    if macd_now is not None: print(f"  {'MACD':<28} {macd_now:.4f}")
    if sig_now  is not None: print(f"  {'MACD Signal':<28} {sig_now:.4f}")
    if hist_now is not None: print(f"  {'MACD Histogram':<28} {hist_now:.4f}")
    if sma20    is not None: print(f"  {'SMA(20)':<28} ${sma20:.2f}")
    if sma50    is not None: print(f"  {'SMA(50)':<28} ${sma50:.2f}")
    if ema12    is not None: print(f"  {'EMA(12)':<28} ${ema12:.2f}")
    if bb_upper is not None: print(f"  {'BB Upper (20,2)':<28} ${bb_upper:.2f}")
    if bb_mid   is not None: print(f"  {'BB Middle':<28} ${bb_mid:.2f}")
    if bb_lower is not None: print(f"  {'BB Lower':<28} ${bb_lower:.2f}")
    if pb       is not None: print(f"  {'BB %B':<28} {pb:.3f}  (0=lower, 0.5=mid, 1=upper)")
    if bw       is not None: print(f"  {'BB Width %':<28} {bw:.2f}%")

    if volumes and len(volumes) == n:
        vwap_vals = vwap(closes, volumes)
        vwap_now = last(vwap_vals)
        if vwap_now:
            print(f"  {'VWAP':<28} ${vwap_now:.2f}")

    print(f"\n  SIGNAL SUMMARY")
    print(f"  {'─'*64}")
    print(f"  {'Indicator':<18} {'Value':>10}  {'Signal':>10}  {'Notes'}")
    print(f"  {'─'*64}")
    for indicator, value, signal, notes in signals:
        icon = "▲" if signal == "BUY" else ("▼" if signal == "SELL" else "─")
        print(f"  {indicator:<18} {value:>10}  {icon+' '+signal:>10}  {notes}")

    bulls = count_bullish(signals)
    bears = count_bearish(signals)
    total_directional = bulls + bears
    if total_directional > 0:
        bull_pct = bulls / total_directional * 100
    else:
        bull_pct = 50

    print(f"\n{'='*64}")
    print(f"  OVERALL SIGNAL: {bulls} BULLISH  vs  {bears} BEARISH")
    bar_bulls = "█" * bulls
    bar_bears = "░" * bears
    print(f"  [{bar_bulls}{bar_bears}]  {bull_pct:.0f}% bullish")
    overall = "BULLISH" if bulls > bears else ("BEARISH" if bears > bulls else "NEUTRAL/MIXED")
    print(f"  VERDICT: {overall}")
    print("=" * 64)

    print(f"\n  NOTE: Technical signals are directional guides, not guarantees.")
    print(f"  Always combine with fundamental analysis and risk management.")
    print(f"  Requires sufficient history: RSI=15+, MACD=27+, SMA50=50+ bars.\n")


if __name__ == "__main__":
    main()
