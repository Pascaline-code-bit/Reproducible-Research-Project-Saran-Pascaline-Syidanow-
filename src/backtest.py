"""
backtest.py

Backtesting utilities
"""


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