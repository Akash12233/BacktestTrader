# init file
from abc import ABC, abstractmethod
import pandas as pd

class IDataFetcher(ABC):
    @abstractmethod
    def get_historical_data(self, ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_fundamental_data(self, ticker: str) -> dict:
        pass