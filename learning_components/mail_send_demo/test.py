import yfinance as yf
import time

def get_near_real_time_price(ticker):
    stock = yf.Ticker(ticker)
    # Fetch 1-minute interval data for the current day
    recent_data = stock.history(period="1d", interval="1m")
    # Return the latest available closing price
    return recent_data['Close'].iloc[-1]

ticker_symbol = "AAPL"
current_price = get_near_real_time_price(ticker_symbol)
print(f"Current price of {ticker_symbol}: ${current_price:.2f}")
