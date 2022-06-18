from collections import defaultdict
from typing import List

from numpy import sort

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        retArr=[]

        nums.sort()
        
        for idx, val in enumerate(nums):

            ##dont use duplicates
            if idx > 0 and val == nums[idx-1]:
                continue

            l = idx+1
            r = len(nums)-1

            while l<r:
                sum = val + nums[l] + nums[r]

                ##Sum too big, decrement the right index to find smaller values
                if sum > 0:
                    r-=1
                ##sum too small, increment left index to find bigger values
                elif sum < 0:
                    l+=1
                else:
                    ##is 0, so append ans but increment left to find possible other answers though
                    retArr.append([val, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l < r:
                        l +=1

        return retArr

g = Solution()
print(g.threeSum([-1,0,1,2,-1,-4]))