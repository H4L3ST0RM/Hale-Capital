
class Position_Data:
    def __init__(self):
        reddit_sentiment = None
        twitter_sentiment = None
        price_ma = None
        trade_volume = None
        VWAP = None
        TWAP = None
        pe_ratio = None
        price_momentum = None
        sector = None
        sector_momentum = None
        symbol = None
        current_price = None
class Market:

    def __init__(self, positions=None):
        positions = positions
        pass


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