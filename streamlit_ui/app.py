import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.algo_trading_system import AlgoTradingSystem
from src.config_loader import load_config

st.title("Akash-BacktestTrader")
config = load_config()
system = AlgoTradingSystem(config)

mode = st.selectbox("Mode", ["backtest", "paper"])
tickers = st.multiselect("Tickers", config['tickers'], default=config['tickers'][:5])
initial_capital = st.number_input("Initial Capital", value=config['initial_capital'])

if st.button("Run"):
    config['tickers'] = tickers
    config['initial_capital'] = initial_capital
    if mode == "backtest":
        ranked = system.backtest_all()
        st.write("Ranked Tickers:", ranked)
    elif mode == "paper":
        ranked = system.backtest_all()
        system.paper_trade(ranked)
        st.image("output/paper_trading_curve.png")