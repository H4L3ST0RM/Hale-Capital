from trader import Trader
from market import Market
import strategies
"""
This the main function for the program.
"""
import os

def main(strategytype,trade_freq):

    PUBLIC_KEY = os.environ.get("ALPACA_PUBLIC_KEY")
    SECRET_KEY = os.environ.get("ALPACA_SECRET_KEY")
    trader = Trader(secret_key=SECRET_KEY,public_key=PUBLIC_KEY)
    market_data = Market(trader.watchlist)

    if strategytype == "mean_reversion":
        strategies.meanReversionStrategy.daily_mean_reversion_strategy(trader, market_data)

    return



