import sys
from typing import List

class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [sys.maxsize] * n
        prices[src] = 0

        for i in range (k+1):

            tmpPrices = prices.copy()

            for sLoc, dLoc, price in flights:

                if prices[sLoc] == sys.maxsize:
                    continue

                if prices[sLoc] + price < tmpPrices[dLoc]:
                    tmpPrices[dLoc] = prices[sLoc] + price

            prices = tmpPrices

        if prices[dst] != sys.maxsize:
            return prices[dst]
        return -1
