import alpaca_trade_api as tradeapi

class Brokerage:

    def __init__(self):
        self.base_url: str
        self.api: tradeapi.REST()
    def connect_api(self,public_key,secret_key):

        self.api = tradeapi.REST(public_key,
                            secret_key,
                            base_url=tradeapi.common.URL('https://paper-api.alpaca.markets'))
        return
    def take_action(self,symbol,action, quantity):
        return self.api.submit_order(
                symbol=symbol,
                side=action,
                type='market',
                qty=quantity,
                time_in_force='day',
                order_class='bracket')


    def update_account_info(self):
        return self.api.get_account()

    def update_account_positions(self):
        return self.api.list_positions()

    def get_watchlist(self):
        return self.api.get_watchlist()

    def get_position_info(self, symbol):
        return