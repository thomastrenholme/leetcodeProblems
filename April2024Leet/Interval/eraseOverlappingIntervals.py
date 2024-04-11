import sys


class Solution:

    def __init__(self):
        self.removed = 0
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        ##O(n(logn) sort by smallest first
        intervals.sort(key=lambda x : x[0])

        chainEnd = -sys.maxsize+1
        lastIntervalSize = -sys.maxsize

        for i in range(len(intervals)):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            currSize = abs(currEnd-currStart)

            if chainEnd <= currStart:
                chainEnd = currEnd
                lastIntervalSize=currSize
            ##Overlap
            else:
                if currEnd < chainEnd:
                    chainEnd = currEnd
                    self.removed+=1
                    lastIntervalSize=currSize
                else:
                    self.removed+=1

        return self.removed

solution = Solution()
print(solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))