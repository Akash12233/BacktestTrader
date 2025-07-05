import pandas as pd
from src.interfaces.i_strategy import IStrategy

class GoldenCrossStrategy(IStrategy):
    def __init__(self, short_window: int = 50, long_window: int = 200):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        signals = pd.Series(0, index=data.index)
        short_ma = data['close'].rolling(window=self.short_window).mean()
        long_ma = data['close'].rolling(window=self.long_window).mean()
        signals[(short_ma > long_ma) & (short_ma.shift(1) <= long_ma.shift(1))] = 1  # Buy
        signals[(short_ma < long_ma) & (short_ma.shift(1) >= long_ma.shift(1))] = -1  # Sell
        return signals