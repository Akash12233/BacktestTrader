# Placeholder for algo_trading_system.py
import multiprocessing
import logging
from src.data.fmp_data_fetcher import FMPDataFetcher
from src.strategies.golden_cross import GoldenCrossStrategy
from src.core.portfolio import Portfolio
from src.core.backtester import Backtester
from src.core.report import ReportGenerator

class AlgoTradingSystem:
    def __init__(self, config):
        self.config = config
        self.data_fetcher = FMPDataFetcher(config['api_key'])
        self.strategy = GoldenCrossStrategy()

    def filter_tickers(self, tickers):
        filtered = []
        for ticker in tickers:
            fundamental_data = self.data_fetcher.get_fundamental_data(ticker)
            if len(fundamental_data) >= 2:
                latest_ebitda = fundamental_data[0]['ebitda']
                previous_ebitda = fundamental_data[1]['ebitda']
                if latest_ebitda > previous_ebitda:
                    filtered.append(ticker)
        return filtered

    def run_backtest(self, ticker):
        data = self.data_fetcher.get_historical_data(ticker, self.config['start_date'], self.config['end_date'])
        if data.empty:
            return ticker, 0.0
        portfolio = Portfolio(self.config['initial_capital'])
        backtester = Backtester(self.strategy, portfolio, {ticker: data}, [ticker])
        backtester.run(mode="backtest")
        final_equity = portfolio.equity_history[-1] if portfolio.equity_history else self.config['initial_capital']
        roi = (final_equity - self.config['initial_capital']) / self.config['initial_capital']
        return ticker, roi

    def backtest_all(self):
        tickers = self.filter_tickers(self.config['tickers'])
        with multiprocessing.Pool() as pool:
            results = pool.map(self.run_backtest, tickers)
        ranked = sorted(results, key=lambda x: x[1], reverse=True)
        print("Backtest Results:")
        for ticker, roi in ranked:
            print(f"{ticker}: ROI = {roi:.2%}")
        return ranked

    def paper_trade(self, ranked_tickers):
        top_tickers = [ticker for ticker, _ in ranked_tickers[:self.config['top_n']]]
        data = {ticker: self.data_fetcher.get_historical_data(ticker, self.config['start_date'], self.config['end_date']) 
                for ticker in top_tickers}
        portfolio = Portfolio(self.config['initial_capital'])
        logging.basicConfig(level=logging.INFO, filename="output/paper_trading.log")
        backtester = Backtester(self.strategy, portfolio, data, top_tickers)
        backtester.run(mode="paper")
        ReportGenerator().generate_equity_curve(portfolio, "paper_trading")

