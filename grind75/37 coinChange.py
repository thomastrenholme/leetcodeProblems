from typing import List

from numpy import sort


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins=sorted(coins)
        coinsUsed = 0
        ##Use biggest coin first
        coinIdx = len(coins)-1
        while amount > 0:
            if coinIdx<0:
                return -1
            currCoin = coins[coinIdx]
            while amount - currCoin >= 0:
                coinsUsed+=1
                amount-=currCoin
            ##Go to next smallest coin
            coinIdx-=1
        return coinsUsed

g = Solution()
print(g.coinChange([2,5,10,1], 27))