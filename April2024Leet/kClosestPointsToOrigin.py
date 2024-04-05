from collections import defaultdict


class Solution:

    def __init__(self):
        self.orderedDistances = []
        self.distanceToXYCoordinate = defaultdict(list)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        for xycoordinate in points:

            ##Only allow unique distances in ordered list, O(1) check
            dist = xycoordinate[0]**2 + xycoordinate[1]**2

            if dist not in self.orderedDistances:
                self.insertIntoOrderedDistances(dist)

            self.distanceToXYCoordinate[dist].append(xycoordinate)

        ans = []

        ## return k closest
        for dist in self.orderedDistances:
            closest = self.distanceToXYCoordinate[dist]

            for point in closest:
                ans.append([point[0], point[1]])
                k-=1
                if k == 0:
                    return ans


    ## O(nlog(n))
    def insertIntoOrderedDistances(self, distanceToInsert: int):

        low = 0
        high = len(self.orderedDistances) -1

        while low <= high:
            mid = (high + low) // 2

            if self.orderedDistances[mid] > distanceToInsert:
                high = mid -1
            else:
                low = mid + 1

        self.orderedDistances = self.orderedDistances[0:low] + [distanceToInsert] + self.orderedDistances[low:len(self.orderedDistances)]

