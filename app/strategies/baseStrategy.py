

import time


class BaseStrategy():
    def __init__(self, trader, market, freq="hourly", budget=None):
        pass


    def strategy(self):
        pass

    def update(self):
        pass

    def execute(self):
        while True:
            self.update()
            self.strategy()
            time.sleep(self.wait)
