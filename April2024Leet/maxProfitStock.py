import sys

## https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        stockLow = sys.maxsize
        stockHigh = -1

        profit = 0

        for i in range(0, len(prices)):

            price = prices[i]

            if price < stockLow:
                stockLow = price
                stockHigh = -1

            elif price > stockHigh:
                stockHigh = price

            ## Profits
            if not(stockHigh == -1) and (stockHigh - stockLow) > profit:
                profit = stockHigh - stockLow

        return profit
