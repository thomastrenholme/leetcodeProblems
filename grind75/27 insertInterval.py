from re import I
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        def binSearchInterval(intervals, startOfNewInterval):

            l = 0
            r = len(intervals)-1
            middle = l + (r-l)//2

            while l<=r:

                middle = l + (r-l)//2
                
                if startOfNewInterval < intervals[middle][0]:
                    r = middle-1
                elif startOfNewInterval > intervals[middle][0]:
                    l = middle +1
                else:
                    ##start of interval is middle
                    return middle
            return l

        modifyIntervalIdx = binSearchInterval(intervals, newInterval[0])

        print("Found modIdxInterval: " + str(modifyIntervalIdx))

        ##merge int1 and int2. Interval 2 is the interval going to be inserted
        def mergeIntervals(int1, int2, intervals):

            ##if in range. 
            if int1[0] <= int2[0] <= int1[1]:

                ##put smallest starting index first
                if int2[0] < int1[0]:
                    int1[0] = int2[0]

                    if int2[1] > int1[1]:
                        int1[]
                else:

                return True
            ##else return false
            return False


        ##now modify interval or insert 
        if intervals[modifyIntervalIdx][0] > newInterval[0] and intervals[modifyIntervalIdx][1] > newInterval[1]:
            ##just insert
            intervals = intervals[0:modifyIntervalIdx+1] + [newInterval] + intervals[modifyIntervalIdx+1:]
        
        elif intervals[modifyIntervalIdx][0] < newInterval[0]:

            if intervals[modifyIntervalIdx][1] <= newInterval[1]:
                intervals[modifyIntervalIdx][1] = newInterval[1]
            ##else
                ##dont modify inside of same interval
        else: ##intervals[modifyIntervalIdx][0] >= newInterval[0]:
            intervals[modifyIntervalIdx][0] = newInterval[0]
            
            if intervals[modifyIntervalIdx][1] <= newInterval[1]:
                intervals[modifyIntervalIdx][1] = newInterval[1]
        return intervals

g = Solution()

print(g.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))