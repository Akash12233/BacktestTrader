# Placeholder for test_portfolio.py
from src.core.portfolio import Portfolio
import pytest

def test_portfolio_buy_sell():
    portfolio = Portfolio(1000)
    portfolio.buy("AAPL", 100, 5)
    assert portfolio.cash == 500
    assert portfolio.positions["AAPL"] == 5
    portfolio.sell("AAPL", 110, 5)
    assert portfolio.cash == 1050
    assert "AAPL" not in portfolio.positions