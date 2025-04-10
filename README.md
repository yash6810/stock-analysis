# Stock Analysis Tool

A Python-based stock analysis tool that provides technical analysis and visualization for stocks using Yahoo Finance data.

## Features

- Fetches historical stock data from Yahoo Finance
- Calculates key technical indicators:
  - Moving Averages (20, 50, and 200-day)
  - Volatility
- Generates comprehensive visualizations:
  - Price and Moving Averages chart
  - Volatility chart
- Provides basic stock statistics:
  - Current price
  - 52-week high/low
  - Volatility metrics
  - Total returns

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yash6810/stock-analysis.git
cd stock-analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the analysis script:
```bash
python stock_analysis.py
```

The script will analyze Tesla (TSLA) and Apple (AAPL) stocks by default, generating analysis plots and printing statistics.

## Output

- Generates PNG files for each analyzed stock (e.g., `TSLA_analysis.png`, `AAPL_analysis.png`)
- Prints key statistics to the console

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## License

MIT License 
