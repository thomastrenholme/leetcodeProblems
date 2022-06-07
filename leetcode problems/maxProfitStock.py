##https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        if not prices or len(prices) <= 1:
            return 0

        left = 0
        right = 0
        maxProfit = 0

        while right < len(prices):

            if prices[left] < prices[right]:

                p = prices[right] - prices[left]
                maxProfit = max(maxProfit, p)

            else:
                left = right
            
            right+=1
        return maxProfit