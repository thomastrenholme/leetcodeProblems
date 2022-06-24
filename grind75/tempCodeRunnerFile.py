from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        currInterval = intervals[0]
        ctr=0
        firstIIntervals=[]

        for i, interval in enumerate(intervals[1:]):

            ##If intersection
            if interval[0] <= currInterval[1]:
                ##Merge intervals
                startInterval = min(interval[0], currInterval[0])
                endInterval = max(interval[1], currInterval[1])
                currInterval = [startInterval, endInterval]

            ##no intersection
            else:
                ##Append curr interval
                firstIIntervals.append(currInterval)
                ##Update curr to this new disconnected interval
                currInterval=interval
            
        firstIIntervals.append(currInterval)
        return firstIIntervals
                

g = Solution()
print(g.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))