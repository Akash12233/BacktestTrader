# Placeholder for test_strategy.py
import pandas as pd
import pytest
from src.strategies.golden_cross import GoldenCrossStrategy

def test_generate_signals():
    data = pd.DataFrame({
        'close': [100] * 200 + [110] * 50  # Crosses above after 200 days
    }, index=pd.date_range("2020-01-01", periods=250))
    strategy = GoldenCrossStrategy()
    signals = strategy.generate_signals(data)
    assert signals.iloc[-1] == 1  # Should generate buy signal