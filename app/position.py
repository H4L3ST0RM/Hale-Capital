"""
The Position_Data object is just a data class, used for storing state data.
"""


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

    def update_position_data(self):
        pass
