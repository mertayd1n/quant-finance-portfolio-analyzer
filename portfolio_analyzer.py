import yfinance as yf
import pandas as pd
import numpy as np


TICKERS = ["AAPL", "MSFT", "NVDA", "AMD", "TSLA"]
START_DATE = "2020-01-01"
END_DATE = "2026-01-01"
RISK_FREE_RATE = 0.02


def download_prices(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)

    if "Close" in data.columns:
        prices = data["Close"]
    else:
        prices = data

    return prices.dropna()


def calculate_returns(prices):
    return prices.pct_change().dropna()


def max_drawdown(series):
    cumulative = (1 + series).cumprod()
    running_max = cumulative.cummax()
    drawdown = cumulative / running_max - 1
    return drawdown.min()


def analyze_assets(returns):
    metrics = pd.DataFrame(index=returns.columns)

    metrics["Annual Return"] = returns.mean() * 252
    metrics["Annual Volatility"] = returns.std() * np.sqrt(252)
    metrics["Sharpe Ratio"] = (
        metrics["Annual Return"] - RISK_FREE_RATE
    ) / metrics["Annual Volatility"]

    metrics["Max Drawdown"] = returns.apply(max_drawdown)

    return metrics


def analyze_portfolio(returns):
    weights = np.array([1 / len(returns.columns)] * len(returns.columns))

    portfolio_returns = returns.dot(weights)

    annual_return = portfolio_returns.mean() * 252
    annual_volatility = portfolio_returns.std() * np.sqrt(252)
    sharpe_ratio = (annual_return - RISK_FREE_RATE) / annual_volatility
    portfolio_drawdown = max_drawdown(portfolio_returns)

    return {
        "Annual Return": annual_return,
        "Annual Volatility": annual_volatility,
        "Sharpe Ratio": sharpe_ratio,
        "Max Drawdown": portfolio_drawdown,
    }


def main():
    prices = download_prices(TICKERS, START_DATE, END_DATE)
    returns = calculate_returns(prices)

    asset_metrics = analyze_assets(returns)
    portfolio_metrics = analyze_portfolio(returns)
    correlation_matrix = returns.corr()

    print("\nAsset Performance Metrics")
    print(asset_metrics.round(4))

    print("\nPortfolio Metrics")
    for key, value in portfolio_metrics.items():
        print(f"{key}: {value:.4f}")

    print("\nCorrelation Matrix")
    print(correlation_matrix.round(4))


if __name__ == "__main__":
    main()
