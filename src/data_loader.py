"""
data_loader.py

Download and preprocess financial data
"""
import yfinance as yf

def download_prices(
    tickers,
    start_date="2010-01-01",
    end_date="2020-01-01"):
    """
    Download adjusted close prices from Yahoo Finance
    """

    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        progress=False
    )

    prices = data["Close"]

    prices = prices.dropna()

    return prices


def compute_returns(prices):
    """
    Compute daily percentage returns
    """

    returns = prices.pct_change()

    returns = returns.dropna()

    return returns