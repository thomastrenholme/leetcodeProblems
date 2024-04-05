from collections import defaultdict

class Solution:

    def __init__(self):
        self.orderedDistances = []
        self.distanceToXYCoordinate = defaultdict(list)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        points.sort(key=lambda x: (x[0]**2 + x[1]**2))

        ans = []
        for xycoordinate in points:
            ans.append(xycoordinate)
            k-=1
            if k == 0:
                return ans