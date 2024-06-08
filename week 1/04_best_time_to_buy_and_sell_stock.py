# You are given an array prices where prices[i]
# is the price of a given stock on the ith day.

# You want to maximize your profit by choosing 
# a single day to buy one stock and choosing a 
# different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep track of the maximum profit and the minimum buying price
        max_profit = 0
        min_buying_price = prices[0]
        
        for price in prices:
            # Update the maximum profit if the current profit is greater
            if price - min_buying_price > max_profit:
                max_profit = price - min_buying_price
            
            # Update the minimum buying price if the current price is lower
            if price < min_buying_price:
                min_buying_price = price
                
        return max_profit