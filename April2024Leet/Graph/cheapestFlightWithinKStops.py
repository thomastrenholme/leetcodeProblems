import sys
from collections import defaultdict
from typing import List


class Solution:

    def __init__(self):
        self.price = sys.maxsize
        self.locationToDestination = defaultdict(set)
        self.locationToDestinationPrices = dict()
        self.minPriceAtLocation = dict()

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        self.maxStops = k

        for flight in flights:
            source = flight[0]
            destination = flight[1]
            price = flight[2]

            self.locationToDestination[source].add(destination)
            self.locationToDestinationPrices[(source, destination)] = price

        self.findCheapestPath(0, 0, src, dst, {})

        if self.price == sys.maxsize:
            return -1
        return self.price

    def findCheapestPath(self, currPrice, currStops, currLocation, destination, tmpMinPriceAtLocation):

        if currLocation == destination:
            if currPrice < self.price:
                self.price = currPrice
                for location in tmpMinPriceAtLocation:
                    self.minPriceAtLocation[location] = tmpMinPriceAtLocation[location]
            return

        if currPrice > self.price or currStops > self.maxStops:
            return

        if currLocation in tmpMinPriceAtLocation and tmpMinPriceAtLocation[currLocation] < currPrice:
            return
        tmpMinPriceAtLocation[currLocation] = currPrice

        if currLocation in self.minPriceAtLocation and self.minPriceAtLocation[currLocation] < currPrice:
            return

        tmpMinPriceAtLocation[currLocation] = currPrice
        locationsAvailable = self.locationToDestination[currLocation]

        for loc in locationsAvailable:
            self.findCheapestPath(currPrice + self.locationToDestinationPrices[(currLocation, loc)], currStops+1, loc, destination, tmpMinPriceAtLocation.copy())


sol = Solution()
print(sol.findCheapestPrice(10, [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]], 6, 0, 7))