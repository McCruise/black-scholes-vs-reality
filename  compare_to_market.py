import numpy as np
import pandas as pd
import yfinance as yf
import scipy.stats as si

# Black-Scholes Formula
def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Black-Scholes formula for European call and put options.
    
    Parameters:
    S - Stock price
    K - Strike price
    T - Time to maturity (years)
    r - Risk-free interest rate
    sigma - Volatility
    option_type - "call" or "put"
    
    Returns:
    Option price
    """
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        return S * si.norm.cdf(d1) - K * np.exp(-r * T) * si.norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * si.norm.cdf(-d2) - S * si.norm.cdf(-d1)

# Fetch stock data
ticker = "AAPL"
stock = yf.Ticker(ticker)

# Get historical stock prices
hist = stock.history(period="1y")

# Compute historical realized volatility (annualized)
returns = np.log(hist["Close"] / hist["Close"].shift(1))
sigma_real = np.std(returns) * np.sqrt(252)

# Get current stock price
S = hist["Close"].iloc[-1]

# Risk-free rate assumption
r = 0.05  # 5%

# Fetch all available option expiration dates
expirations = stock.options

# Store results
option_data = []

# Loop through all expiration dates
for exp in expirations:
    try:
        # Fetch option chain for this expiration
        option_chain = stock.option_chain(exp)
        calls = option_chain.calls
        # puts = option_chain.puts

        # Loop through all strike prices
        for _, row in calls.iterrows():
            K = row["strike"]  # Strike price
            market_price = row["lastPrice"]  # Market option price
            
            # Calculate time to maturity in years
            T = (pd.to_datetime(exp) - pd.Timestamp.today()).days / 365

            if T > 0:  # Ensure maturity is valid
                # Compute Black-Scholes call price
                bs_price = black_scholes(S, K, T, r, sigma_real, "call")

                # Store data
                option_data.append([exp, K, market_price, bs_price])

    except Exception as e:
        print(f"Skipping {exp} due to error: {e}")

# Convert to DataFrame
df = pd.DataFrame(option_data, columns=["Maturity", "Strike", "Market Price", "Black-Scholes Price"])

# Display table in terminal
# print(df)
print(df.to_string(index=False))

# Save to CSV for easy viewing
df.to_csv("option_comparison.csv", index=False)
print("Results saved to option_comparison.csv")
