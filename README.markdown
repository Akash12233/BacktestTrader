# BacktestTrader

A modular algorithmic trading system for backtesting and paper trading, designed to analyze S&P 500 tickers with a blend of fundamental and technical strategies.

## Overview
"BacktestTrader" is a Python-based project that simulates trading strategies on historical data, ranks assets by return on investment (ROI), and supports paper trading. It leverages multiprocessing for efficiency and includes a Streamlit UI for interactivity. Inspired by the WUSIF hackathon, this system mirrors workflows used by quantitative trading firms for research and alpha discovery.

## Features
- **Multi-Asset Backtesting**: Backtests 10–50 tickers simultaneously using multiprocessing.
- **Fundamental + Technical Analysis**: Filters for positive EBITDA growth and uses a golden cross strategy (50-day vs. 200-day MA).
- **Performance Ranking**: Ranks tickers by ROI for top performers.
- **Paper Trading Simulation**: Mimics live trading in a risk-free environment.
- **Visualization**: Generates equity curve plots with Matplotlib.
- **Modular Design**: Built with OOP and LLD principles for extensibility.

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/BacktestTrader.git
   cd BacktestTrader
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure API Key**:
   - Obtain a free API key from [Financial Modeling Prep](https://financialmodelingprep.com/).
   - Update `config.yaml` with your API key and preferred tickers.
4. **Create Output Directory**:
   ```bash
   mkdir output
   ```

## Usage
- **Backtest Mode**:
  ```bash
  python main.py --mode backtest
  ```
  - Analyzes historical data and ranks tickers by ROI.
- **Paper Trading Mode**:
  ```bash
  python main.py --mode paper
  ```
  - Simulates live trading and saves an equity curve.
- **Streamlit UI**:
  ```bash
  streamlit run streamlit_ui/app.py
  ```
  - Launches an interactive interface to run backtests or paper trading.

## Project Structure
- `src/`: Core logic including strategies, data fetchers, and backtesting.
- `tests/`: Unit tests for validation.
- `output/`: Stores generated plots (e.g., equity curves).
- `streamlit_ui/`: Interactive UI with Streamlit.
- `config.yaml`: Configuration file for API keys and settings.
- `requirements.txt`: Dependency list.
- `main.py`: Command-line entry point.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License
[MIT License](LICENSE) - Feel free to modify and distribute, but include the original license.

## Acknowledgments
- Built with inspiration from the WUSIF hackathon.
- Utilizes the Financial Modeling Prep API for data.