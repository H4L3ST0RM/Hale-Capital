import time
"""
Simplistic Implementation of mean-reversion strategy.
"""
def daily_mean_reversion_strategy(trader, market, budget):
    trader.update()
    min_budget = trader.account_info.account_value - budget
    while min_budget < trader.account_info.account_value - budget:
        for stock in trader.watchlist:

            market.update(stock.symbol)
            # If moving average < current price then sell
            if market.positions_data[stock.symbol].price_ma < market.positions_data[stock.symbol].current_price:
                trader.sell(stock.symbol,5)

            # If moving average > current price then buy
            elif market.positions_data[stock.symbol].price_ma > market.positions_data[stock.symbol].current_price:
                trader.buy(stock.symbol,5)
            trader.update()
            time.sleep(60*60*24)

    return #metrics
