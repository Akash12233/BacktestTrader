# init file
from abc import ABC, abstractmethod
import pandas as pd

class IStrategy(ABC):
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        pass