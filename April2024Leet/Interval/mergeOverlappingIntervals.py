import sys


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key=lambda x: x[0])

        lastEnd = -sys.maxsize
        ans = []
        currIntervalIndex = -1

        for i in range(len(intervals)):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]

            if currStart > lastEnd:
                lastEnd = currEnd
                ans.append(intervals[i])
                currIntervalIndex+=1
            ##Overlap
            else:
                lastEnd= max(currEnd, lastEnd)
                ans[currIntervalIndex] = [ans[currIntervalIndex][0], lastEnd]

        return ans

sol = Solution()
print(sol.merge([[1,4],[2,3]]))