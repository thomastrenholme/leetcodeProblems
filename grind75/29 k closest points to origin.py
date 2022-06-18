from collections import defaultdict
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ##Go through points and calculate distance from each point to the origin.
        ##Put this distances into a dictionary where the tuple (x, y) is the key and the
        ##value is the distance. 
        ##At the end, we take the values and reverse sort then and return the first k.

        XYtoDistDict = {}
        distToXYDict = defaultdict(list)
        for xyCoord in points:

            x=xyCoord[0]
            y=xyCoord[1]

            dist = sqrt( (x)**2 + (y)**2) 
            
            XYtoDistDict[(x, y)] = dist
            distToXYDict[dist].append([x, y])

        res=[]
        for dist in sorted(XYtoDistDict.values()):

            for xy in distToXYDict[dist]:
                if k==0:
                    return res
                res.append(xy)
                k-=1
        return res

    ##official solution from leetcode
    class Solution:
        def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            # Sort the list with a custom comparator function
            points.sort(key=self.squared_distance)
            
            # Return the first k elements of the sorted list
            return points[:k]
        
        def squared_distance(self, point: List[int]) -> int:
            """Calculate and return the squared Euclidean distance."""
            return point[0] ** 2 + point[1] ** 2


