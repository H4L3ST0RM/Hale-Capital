
from trader import Trader
from market_env import Market
from config import *
from strategy import Strategy

def main():
    PUBLIC_KEY = "PKT1MRL4AFJUQNNH43Y6"
    SECRET_KEY = "BKC0blpd2KEi4WllW2pqmO87OXBP3Pl1mikZo2Zm"
    strategy = Strategy()
    trader = Trader(secret_key=SECRET_KEY,public_key=PUBLIC_KEY)
    market = Market()
    while True:
        for position in trader.get_watchlist():
            pos_data = market.get_data()
            strategy = Strategy(Trader, position, pos_data)
