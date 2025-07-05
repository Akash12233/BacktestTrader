class Portfolio:
    def __init__(self, initial_capital: float):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.positions = {}  # ticker: shares
        self.equity_history = []

    def buy(self, ticker: str, price: float, shares: int):
        cost = price * shares
        if cost <= self.cash:
            self.cash -= cost
            self.positions[ticker] = self.positions.get(ticker, 0) + shares

    def sell(self, ticker: str, price: float, shares: int):
        if ticker in self.positions and self.positions[ticker] >= shares:
            revenue = price * shares
            self.cash += revenue
            self.positions[ticker] -= shares
            if self.positions[ticker] == 0:
                del self.positions[ticker]

    def update_equity(self, current_prices: dict):
        equity = self.cash
        for ticker, shares in self.positions.items():
            if ticker in current_prices:
                equity += shares * current_prices[ticker]
        self.equity_history.append(equity)