import yfinance as yf
import pandas as pd

def fetch_close(ticker: str, date: str) -> float:
    # pull historical close for given date
    df = yf.download(ticker, start=date, end=date)
    return df['Close'].iloc[0]

# add functions for yield curves and correlation