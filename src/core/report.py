import matplotlib
matplotlib.use('Agg')  # Set headless backend
import matplotlib.pyplot as plt
from src.core.portfolio import Portfolio

class ReportGenerator:
    def generate_equity_curve(self, portfolio: Portfolio, filename: str):
        plt.figure(figsize=(10, 6))
        plt.plot(portfolio.equity_history)
        plt.title(f"Equity Curve - {filename}")
        plt.xlabel("Time")
        plt.ylabel("Equity")
        plt.savefig(f"output/{filename}_curve.png")
        plt.close()