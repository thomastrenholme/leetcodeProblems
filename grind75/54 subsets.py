from re import sub
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        if not nums:
            return nums
        res = [[]]

        def dfsSubsets(nums, subset, index):
            res.append(subset)

            for n in range(index, len(nums)):
                dfsSubsets(nums, subset+[nums[n]],n+1)

        for n in range(len(nums)):
            dfsSubsets(nums, [nums[n]], n+1)
        return res

g = Solution()
print(g.subsets([1,2,3]))