# Placeholder for main.py
import argparse
from src.algo_trading_system import AlgoTradingSystem
from src.config_loader import load_config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WUSIF-BacktestTrader")
    parser.add_argument("--mode", choices=["backtest", "paper"], default="backtest", help="Run mode")
    args = parser.parse_args()
    
    config = load_config()
    system = AlgoTradingSystem(config)
    
    if args.mode == "backtest":
        ranked_tickers = system.backtest_all()
    elif args.mode == "paper":
        ranked_tickers = system.backtest_all()
        system.paper_trade(ranked_tickers)