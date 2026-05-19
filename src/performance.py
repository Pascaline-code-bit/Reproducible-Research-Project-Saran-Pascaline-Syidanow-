"""
performance.py

Performance metrics
"""

import numpy as np


def annualized_return(
    returns,
    periods=252
):
    """
    Compute annualized return
    """

    return returns.mean() * periods


def annualized_volatility(
    returns,
    periods=252
):
    """
    Compute annualized volatility
    """

    return returns.std() * np.sqrt(periods)


def sharpe_ratio(
    returns,
    risk_free_rate=0.0,
    periods=252
):
    """
    Compute annualized Sharpe ratio
    """

    excess_returns = (
        returns - risk_free_rate / periods
    )

    ann_return = excess_returns.mean() * periods

    ann_vol = excess_returns.std() * np.sqrt(periods)

    return ann_return / ann_vol


def max_drawdown(
    cumulative_returns
):
    """
    Compute maximum drawdown
    """

    running_max = cumulative_returns.cummax()

    drawdown = (
        cumulative_returns - running_max
    ) / running_max

    return drawdown.min()