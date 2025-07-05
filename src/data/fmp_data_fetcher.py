import requests
import pandas as pd
from src.interfaces.i_data_fetcher import IDataFetcher

class FMPDataFetcher(IDataFetcher):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_historical_data(self, ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
        url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={start_date}&to={end_date}&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        if 'historical' not in data:
            return pd.DataFrame()
        df = pd.DataFrame(data['historical'])
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        return df[['close']]

    def get_fundamental_data(self, ticker: str) -> dict:
        url = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit=120&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data