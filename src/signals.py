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