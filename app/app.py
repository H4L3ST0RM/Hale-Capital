from trader import Trader
from market import Market
import strategies
"""
This the main function for the program.
"""
def main(strategytype,trade_freq):
    PUBLIC_KEY = "PKT1MRL4AFJUQNNH43Y6"
    SECRET_KEY = "BKC0blpd2KEi4WllW2pqmO87OXBP3Pl1mikZo2Zm"

    trader = Trader(secret_key=SECRET_KEY,public_key=PUBLIC_KEY)
    market_data = Market(trader.watchlist)

    if strategytype == "mean_reversion":
        strategy = strategies.meanReversionStrategy.MeanReversionStrategy(trader,market_data,freq=trade_freq)

    strategy.execute(trader,market_data)

    return



