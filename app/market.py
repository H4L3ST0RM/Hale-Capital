from position import Position_Data
"""
The market object is designed to hold all data necessary for the Trader to make a decision on.

From an RL perspective, this object contains the current state of the environment.
"""
class Market:
    def __init__(self, positions=None):
        self.positions_data = {}
        for pos in positions:
            sym = pos.symbol
            self.positions_data[sym] = self.update(sym)

        pass

    def update(self,symbol):
        cur_price = pos.current_price
        red_sent = self.get_reddit_sentiment(sym)
        twit_sent = self.get_twitter_sentiment(sym)
        ma = self.get_moving_average(sym)
        vwap = self.get_volume_weighted_average_price(sym)
        twap = self.get_time_weighted_average_price(sym)
        pe = self.get_price_to_earnings_ratio(sym)
        mom = self.get_momentum(sym)
        sector = self.get_sector(sym)
        sec_mom = self.get_sector_momentum(sym)
        vol = self.get_trade_volume(sym)
        return Position_Data(reddit_sentiment = red_sent,
                                                    twitter_sentiment = twit_sent,
                                                    price_ma = ma,
                                                    trade_volume = vol,
                                                    VWAP = vwap,
                                                    TWAP = twap,
                                                    pe_ratio = pe,
                                                    price_momentum = mom,
                                                    sector = sector,
                                                    sector_momentum = sec,
                                                    symbol = sym,
                                                    current_price = cur_price)

    def get_market_price(self, symbol):
        pass

    def get_twitter_sentiment(self,symbol):
        pass

    def get_reddit_sentiment(self,symbol):
        pass
    ############################################################
    # One time pull of historical data to get initial moving average.
    # Subsequent moving averages are calculated by the following formula
    # ma_n = (ma_(n-1) * 199) + previous_close_price
    ############################################################
    def get_moving_average(self,symbol):
        pass

    def get_trade_volume(self,symbol):
        pass

    def get_volume_weighted_average_price(self,symbol):
        pass

    def get_time_weighted_average_price(self):
        pass

    def get_price_to_earnings_ratio(self):
        pass

    def get_momentum(self):
        pass

    def get_sector_momentum(self):
        pass

    def get_symbol_data(self,symbol):
        pass