import strategies
import brokerage


class Trader:
    def __init__(self, secret_key,public_key,positions=None, account_value=None):

        self.__sec_key = secret_key
        self.__pub_key = public_key
        self.brokerage = brokerage().connect_api(self.__pub_key,self.__sec_key)
        self.brokerage.connect_api()
        self.positions = self.brokerage.update_account_positions()
        self.account_info = self.update_account_info()
        self.watchlist = self.get_watchlist()

    def buy(self, symbol,quantity):
        status = self.brokerage.take_action(symbol=symbol,action="buy", quantity=quantity)
        self.positions = self.brokerage.update_account_positions()
        self.account_info = self.brokerage.update_account_info()
        return

    def sell(self, symbol, quantity, price):
        status = self.brokerage.take_action(symbol=symbol,action="sell", quantity=quantity)
        self.positions = self.brokerage.update_account_positions()
        self.account_info = self.brokerage.update_account_info()
        return

    def update_account_info(self):
        self.account_info = self.brokerage.update_account_info()
        return

    def get_watchlist(self):
        self.watchlist = self.get_watchlist()
        return