from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numsValuetoIdxDict = defaultdict(list)  
        for i in range(0, len(nums)):
            numsValuetoIdxDict[nums[i]].append(i)

        retArr = []
        for value in numsValuetoIdxDict:

            desiredVal = target-value

            if not desiredVal in numsValuetoIdxDict:
                continue
            else:
                if desiredVal != value:
                    return [numsValuetoIdxDict[value][0], numsValuetoIdxDict[desiredVal][0]]
                elif desiredVal == value and len(numsValuetoIdxDict[desiredVal]) > 1:
                    return [numsValuetoIdxDict[value][0], numsValuetoIdxDict[desiredVal][1]]
        return retArr

g = Solution()

print(g.twoSum([2,7,11,15], 9))