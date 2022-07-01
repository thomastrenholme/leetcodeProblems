from re import sub
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[], nums]

        def getSubsets(arr, subset, index):
            print("subset: " + str(subset))
            if len(arr)==0:
                res.append(subset)
                return
            for newElemIdx in range(index, len(arr)):
                getSubsets(arr[0:newElemIdx] + arr[newElemIdx+1:], subset+[arr[newElemIdx]], newElemIdx)
        
        for n in range(len(nums)):
            getSubsets(nums[0:n] + nums[n+1:], [nums[n]], n)
        
        return res

g = Solution()
print(g.subsets(nums = [1,2,3]))