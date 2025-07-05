# Placeholder for test_backtester.py
import logging
from src.interfaces.i_strategy import IStrategy
from src.core.portfolio import Portfolio

class Backtester:
    def __init__(self, strategy: IStrategy, portfolio: Portfolio, data: dict, tickers: list):
        self.strategy = strategy
        self.portfolio = portfolio
        self.data = data  # dict of ticker: DataFrame
        self.tickers = tickers

    def run(self, mode: str = "backtest"):
        # Align dates across all tickers
        dates = sorted(set.intersection(*[set(df.index) for df in self.data.values()]))
        for date in dates:
            current_prices = {}
            for ticker in self.tickers:
                if date in self.data[ticker].index:
                    current_prices[ticker] = self.data[ticker].loc[date, 'close']
                    signal = self.strategy.generate_signals(self.data[ticker]).loc[date]
                    if signal == 1:
                        cash_to_spend = self.portfolio.cash * 0.1
                        shares = int(cash_to_spend / current_prices[ticker])
                        if shares > 0:
                            self.portfolio.buy(ticker, current_prices[ticker], shares)
                            if mode == "paper":
                                logging.info(f"{date}: Buy {shares} shares of {ticker} at {current_prices[ticker]}")
                    elif signal == -1 and ticker in self.portfolio.positions:
                        shares = self.portfolio.positions[ticker]
                        self.portfolio.sell(ticker, current_prices[ticker], shares)
                        if mode == "paper":
                            logging.info(f"{date}: Sell {shares} shares of {ticker} at {current_prices[ticker]}")
            self.portfolio.update_equity(current_prices)
            if mode == "paper" and current_prices:
                logging.info(f"{date}: Equity = {self.portfolio.equity_history[-1]}")