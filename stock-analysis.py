import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set the style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_theme()

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch stock data from Yahoo Finance"""
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df

def calculate_moving_averages(df, windows=[20, 50, 200]):
    """Calculate moving averages for different windows"""
    for window in windows:
        df[f'MA_{window}'] = df['Close'].rolling(window=window).mean()
    return df

def calculate_volatility(df, window=20):
    """Calculate rolling volatility"""
    df['Volatility'] = df['Close'].pct_change().rolling(window=window).std() * np.sqrt(252)
    return df

def plot_stock_analysis(df, ticker):
    """Create comprehensive stock analysis plots"""
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10), height_ratios=[2, 1])
    
    # Plot 1: Price and Moving Averages
    ax1.plot(df.index, df['Close'], label='Close Price', alpha=0.7)
    for ma in [20, 50, 200]:
        if f'MA_{ma}' in df.columns:
            ax1.plot(df.index, df[f'MA_{ma}'], label=f'{ma}-day MA', alpha=0.7)
    
    ax1.set_title(f'{ticker} Stock Price and Moving Averages')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price (USD)')
    ax1.legend()
    ax1.grid(True)
    
    # Plot 2: Volatility
    ax2.plot(df.index, df['Volatility'], label='Volatility', color='red', alpha=0.7)
    ax2.set_title(f'{ticker} Rolling Volatility (20-day)')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Volatility')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig(f'{ticker}_analysis.png')
    plt.close()

def main():
    # Define the stocks to analyze
    stocks = ['TSLA', 'AAPL']
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)  # 1 year of data
    
    for ticker in stocks:
        print(f"\nAnalyzing {ticker}...")
        
        # Fetch data
        df = fetch_stock_data(ticker, start_date, end_date)
        
        # Calculate indicators
        df = calculate_moving_averages(df)
        df = calculate_volatility(df)
        
        # Create plots
        plot_stock_analysis(df, ticker)
        
        # Print some basic statistics
        print(f"\n{ticker} Statistics:")
        print(f"Current Price: ${df['Close'].iloc[-1]:.2f}")
        print(f"52-week High: ${df['High'].max():.2f}")
        print(f"52-week Low: ${df['Low'].min():.2f}")
        print(f"Current Volatility: {df['Volatility'].iloc[-1]:.2%}")
        
        # Calculate and print returns
        total_return = (df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0] * 100
        print(f"Total Return: {total_return:.2f}%")

if __name__ == "__main__":
    main() 
