import yfinance as yf
import time

# Define the stock ticker and target price
ticker_symbol = 'AAPL'
target_price = 225

# Create the Ticker object
ticker = yf.Ticker(ticker_symbol)

# Start the monitoring loop
while True:
    # Get the current stock price
    stock_price = ticker.history(period="1d")['Close'].iloc[-1]
    print(f"Current AAPL price: ${stock_price:.2f}")
    
    # Check if it has reached or exceeded the target price
    if stock_price >= target_price:
        print(f"AAPL has reached the target price of ${target_price}!")
        break
    
    # Wait before checking again
    time.sleep(60)  # Check every 60 seconds (adjust as needed)