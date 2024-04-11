import bisect
from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        numsToIndicies = defaultdict(set)

        for i in range(len(nums)):
            numsToIndicies[nums[i]].add(i)

        for n in nums:
            targetVal = target - n

            ## Special case if targetVal == the number we are checking.
            if targetVal == n:
                if len(numsToIndicies[targetVal]) > 1:
                    setIterator = iter(numsToIndicies[targetVal])
                    return [next(setIterator), next(setIterator)]

            elif targetVal in numsToIndicies:
                ## Return first (only) element of the set for the numsToIndicies dict entry for n & targetVal
                return [next(iter(numsToIndicies[n])), next(iter(numsToIndicies[targetVal]))]

sol = Solution()
print(sol.twoSum([-10,-1,-18,-19], -19))