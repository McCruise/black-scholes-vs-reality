# Black-Scholes vs Market Prices

## Overview
This project compares Black-Scholes theoretical option pricing with real market option prices fetched from Yahoo Finance. It calculates Black-Scholes prices using **historical realized volatility** and compares them with actual option prices.

## Features
- Fetches **real market option prices** from Yahoo Finance.
- Computes **historical volatility** from stock data.
- Prices options using the **Black-Scholes model**.
- Compares **market prices vs. model prices**.
- Displays a full table of **maturities, strikes, market vs. theoretical prices**.

## How to Run
1. Install dependencies:
   ```bash
   pip install numpy scipy yfinance==0.2.54 pandas matplotlib
