from typing import List

from numpy import sort


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        currInterval = intervals[0]
        res=[]

        for interval in intervals[1:]:

            ##If intersection
            if interval[0] <= currInterval[1]:
                ##Merge intervals
                startInterval = min(interval[0], currInterval[0])
                endInterval = max(interval[1], currInterval[1])
                currInterval = [startInterval, endInterval]

            ##no intersection
            else:
                ##Append curr interval
                res.append(currInterval)
                ##Update curr to this new disconnected interval
                currInterval=interval
            
        res.append(currInterval)
        return res
                

g = Solution()
print(g.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))