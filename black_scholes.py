 
import numpy as np
import scipy.stats as si

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

if __name__ == "__main__":
    # Example usage
    S, K, T, r, sigma = 100, 105, 1, 0.05, 0.2
    call_price = black_scholes(S, K, T, r, sigma, "call")
    put_price = black_scholes(S, K, T, r, sigma, "put")

    print(f"Call Option Price: {call_price:.2f}")
    print(f"Put Option Price: {put_price:.2f}")
