import yfinance as yf
import pandas as pd
import numpy as np


TICKERS = ["AAPL", "AMZN", "GOOGL", "META", "MSFT", "NVDA", "TSLA"]
START_DATE = "2020-01-01"
END_DATE = "2026-01-01"
RISK_FREE_RATE = 0.02
NUMBER_OF_PORTFOLIOS = 10000


def download_prices(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)

    if "Close" in data.columns:
        prices = data["Close"]
    else:
        prices = data

    return prices.dropna()


def calculate_returns(prices):
    return prices.pct_change().dropna()


def generate_random_portfolios(returns):
    results = []

    mean_returns = returns.mean() * 252
    covariance_matrix = returns.cov() * 252
    number_of_assets = len(returns.columns)

    for _ in range(NUMBER_OF_PORTFOLIOS):
        weights = np.random.random(number_of_assets)
        weights = weights / np.sum(weights)

        portfolio_return = np.dot(weights, mean_returns)
        portfolio_volatility = np.sqrt(
            np.dot(weights.T, np.dot(covariance_matrix, weights))
        )
        sharpe_ratio = (portfolio_return - RISK_FREE_RATE) / portfolio_volatility

        portfolio_data = {
            "Return": portfolio_return,
            "Volatility": portfolio_volatility,
            "Sharpe Ratio": sharpe_ratio,
        }

        for ticker, weight in zip(returns.columns, weights):
            portfolio_data[f"{ticker} Weight"] = weight

        results.append(portfolio_data)

    return pd.DataFrame(results)


def main():
    prices = download_prices(TICKERS, START_DATE, END_DATE)
    returns = calculate_returns(prices)

    portfolios = generate_random_portfolios(returns)

    max_sharpe_portfolio = portfolios.loc[portfolios["Sharpe Ratio"].idxmax()]
    min_volatility_portfolio = portfolios.loc[portfolios["Volatility"].idxmin()]

    print("\nMaximum Sharpe Ratio Portfolio")
    print(max_sharpe_portfolio.round(4))

    print("\nMinimum Volatility Portfolio")
    print(min_volatility_portfolio.round(4))

    print("\nTop 5 Portfolios by Sharpe Ratio")
    print(portfolios.sort_values("Sharpe Ratio", ascending=False).head().round(4))


if __name__ == "__main__":
    main()
