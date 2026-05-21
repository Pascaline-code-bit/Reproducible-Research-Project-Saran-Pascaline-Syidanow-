"""
backtest.py

Backtesting utilities
"""
import numpy as np

def compute_strategy_returns(
    returns,
    signals
):
    """
    Compute returns from strategy
    """

    strategy_returns = signals * returns

    strategy_returns = strategy_returns.dropna()

    return strategy_returns

def compute_overlapping_returns(returns, signals_dict):
    """
    Average signals across multiple horizons
    """

    combined = None

    for sig in signals_dict.values():
        strat = sig * returns

        if combined is None:
            combined = strat
        else:
            combined += strat

    combined = combined / len(signals_dict)

    return combined

def compute_vol_scaled_returns(returns, signals, target_vol=0.1):
    """
    Volatility scaling
    """

    vol = returns.rolling(60).std()

    scaling = target_vol / vol
    scaling = scaling.clip(lower=0.8,upper=1.2) #Results vary massively by scaling

    scaled_returns = signals * scaling * returns

    return scaled_returns

def aggregate_portfolio_returns(
    strategy_returns
):
    """
    Aggregate returns across assets
    """

    portfolio_returns = strategy_returns.mean(axis=1)

    return portfolio_returns


def compute_cumulative_returns(
    portfolio_returns
):
    """
    Compute cumulative portfolio performance
    """

    cumulative_returns = (
        1 + portfolio_returns
    ).cumprod()

    return cumulative_returns