# quant-finance-portfolio-analyzer
A Python project for analyzing stock portfolio returns, risk, volatility, Sharpe ratio and drawdowns.
# Quant Finance Portfolio Analyzer

A Python-based quantitative finance project that analyzes stock portfolio performance using historical market data.

This project calculates key financial metrics such as annual return, annual volatility, Sharpe ratio, maximum drawdown, and correlation between assets.

## Project Overview

The goal of this project is to demonstrate practical quantitative finance skills using Python, financial data analysis, and portfolio risk-return measurement.

The project analyzes a sample portfolio consisting of major technology stocks:

- AAPL
- MSFT
- NVDA
- AMD
- TSLA

## Features

- Download historical stock price data
- Calculate daily returns
- Compute annualized return
- Compute annualized volatility
- Calculate Sharpe Ratio
- Measure Maximum Drawdown
- Analyze asset correlation
- Evaluate equal-weighted portfolio performance

## Technologies Used

- Python
- pandas
- numpy
- yfinance

## Key Metrics

### Annual Return

Measures the average yearly return of each asset.

### Annual Volatility

Measures the yearly risk or price fluctuation of each asset.

### Sharpe Ratio

Measures risk-adjusted return.

Higher Sharpe Ratio generally means better return per unit of risk.

### Maximum Drawdown

Measures the largest historical decline from peak to bottom.

### Correlation Matrix

Shows how strongly assets move together.

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
