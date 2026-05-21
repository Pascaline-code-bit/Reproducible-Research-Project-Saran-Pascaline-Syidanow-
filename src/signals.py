"""
signals.py

Momentum signal generation
"""
import numpy as np

def compute_momentum_signal(
    prices,
    lookback=252
):
    """
    Compute time-series momentum signals

    Signal:
        +1 if past return > 0
        -1 otherwise
    """

    past_returns = prices.pct_change(lookback)

    signals = np.sign(past_returns)

    signals = signals.shift(1)

    return signals

def compute_multi_horizon_signals(prices):
    """
    Compute signals for multiple horizons:
    1, 3, 6, 12 months
    """

    horizons = [21, 63, 126, 252]

    signals = {}

    for h in horizons:
        sig = np.sign(prices.pct_change(h)).shift(1)
        signals[h] = sig

    return signals