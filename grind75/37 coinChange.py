import sys
from typing import List

from numpy import sort
from sklearn.metrics import ConfusionMatrixDisplay


class Solution:
    leastCoinsUsed=sys.maxsize
    coinAmtToNumUsed = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dpArray = [sys.maxsize] * (amount+1)

        dpArray[0] = 0

        for amtLeft in range(1, amount+1):
            
            for c in coins:

                if amtLeft - c >= 0:
                    dpArray[amtLeft] = min(dpArray[amtLeft], 1 + dpArray[amtLeft-c])
        return dpArray[amount] if dpArray[amount] != sys.maxsize else -1



        # ##Make sure when going through coins, largest is used first.
        # coins = sorted(coins, reverse=True)
        # def coinDfs(coin, amtLeft, numCoinsUsed):
        #     if amtLeft > 0:
        #         ##if amt left already computed
        #         if amtLeft in self.coinAmtToNumUsed:
        #             return self.coinAmtToNumUsed[amtLeft]
                
        #         ##Else, calculate min for current amt Left
        #         potentialMins=[sys.maxsize] * len(coins)
        #         for coin in range(len(coins)):
        #             potentialMins[coin] = coinDfs(coins[coin], amtLeft-coin, numCoinsUsed+1)
        #         self.coinAmtToNumUsed[amtLeft] = min(potentialMins)
        #         return min(potentialMins)
        #     elif amtLeft == 0:
        #         self.coinAmtToNumUsed[coin] = 1
        #         return numCoinsUsed
        #     else:
        #         ##Unreachable 0 with current coin
        #         self.coinAmtToNumUsed[coin] = sys.maxsize
        #         return sys.maxsize

        # potentialMins = [sys.maxsize] * len(coins)
        # for c in range(len(coins)):
        #     potentialMins[c] = coinDfs(coins[c], amount-coins[c], 1)
        
        # return min[potentialMins] if not min[potentialMins] == sys.maxsize else 0
g = Solution()
print(g.coinChange([1, 2, 5], 20))