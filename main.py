# %%
import yfinance as yf
#help(yf)
import pandas as pd

# %%
def fetch_prices(ticker, start_date):
    stock = yf.Ticker(ticker)
    prices = stock.history(start=start_date, auto_adjust=True)
    return prices


result = fetch_prices("AAPL", "2024-01-01")

#print(result.head())

# %%
stock = yf.Ticker("AAPL")
help(stock.history)
# %%
