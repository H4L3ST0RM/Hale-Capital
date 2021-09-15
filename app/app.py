
from trader import Trader
from market import Market


def main(strategy):
    PUBLIC_KEY = "PKT1MRL4AFJUQNNH43Y6"
    SECRET_KEY = "BKC0blpd2KEi4WllW2pqmO87OXBP3Pl1mikZo2Zm"
    trader = Trader(secret_key=SECRET_KEY,public_key=PUBLIC_KEY)
    market_data = Market(trader.watchlist)
    strategy.execute(trader,market_data)
    return

"""
multi-arm bandit problem
Environment variables:
- Ticker data
    - Current stock price
    - Moving Average
    - VWAP
    - TWAP
    - Twitter Sentiment
    - Reddit Sentiment
    - Momentum
    - Trend
    - Sector Momentum
    - Sector Trend
    - P/E
    - Sector P/E
    - EPS
    - Acid Test
    - Working Capital Ratio
    - Debt-Equity Ratio
- Account data
- 
Action: [Stocks x actions]
 
 
 step 1: Given inputs for given time step of each stock, select stock+action
 step 2: Select amount [based on confidence of action
 step 3: execute
"""


