

import time
from baseStrategy import BaseStrategy


# WORK IN PROGRESS
class MeanReversionStrategy(BaseStrategy):
    def __init__(self, trader, market, freq="hourly", budget=None):
        self.trader = trader
        self.market = market
        self.budget = budget
        if freq == "minute":
            self.wait = 60 # 1 minute
        elif freq == "hourly":
            self.wait = 60 * 60 # 1 hour
        elif freq == "daily":
            self.wait = 60 * 60 * 24 # Daily


    def strategy(self):
        for stock in self.watchlist:
            self.market.update(stock.symbol)
            if self.market.positions[self.symbol].price_ma < self.market.positions[self.symbol].current_price:
                self.trader.buy(self.symbol,5)
            elif self.market.positions[self.symbol].price_ma > self.market.positions[self.symbol].current_price:
                self.trader.sell(self.symbol,5)
        return

    def update(self):
        self.trader.update()
        pass

    def execute(self):
        while True:
            self.update()
            self.strategy()
            time.sleep(self.wait)
