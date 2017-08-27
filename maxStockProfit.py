"""
This calculates the maximum stock profit that one could get from buying and selling stock in one day between opening and closing.

I get data in the form of a list.

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

I should be able to do this by going through the list only once. That means I need to keep track of the minimum stock price and the maximum profit as I go through the list. I also need to return a negative value if the stock price goes down all day, this tells the user if they lost money during the day.
"""

def max_profit(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise IndexError('length of stock prices must have two elements to calculate a profit')
    minPrice = stock_prices_yesterday[0]
    maxProfit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    for index,val in enumerate(stock_prices_yesterday):
        if index == 0:
            continue
        potentialProfit = val - minPrice
        maxProfit = max(maxProfit,potentialProfit)
        minPrice = min(minPrice,val)
    return maxProfit


stock_prices_yesterday = [10, 7, 5, 4, 2, 0]
profit = max_profit(stock_prices_yesterday)
