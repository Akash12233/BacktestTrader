import pandas as pd
from src.strategies.golden_cross import GoldenCrossStrategy
from src.core.portfolio import Portfolio
from src.core.backtester import Backtester

def test_backtester():
    data = {"AAPL": pd.DataFrame({'close': [100] * 200 + [110] * 50}, 
                                 index=pd.date_range("2020-01-01", periods=250))}
    portfolio = Portfolio(1000)
    strategy = GoldenCrossStrategy()
    backtester = Backtester(strategy, portfolio, data, ["AAPL"])
    backtester.run()
    assert len(portfolio.equity_history) == 250