from typing import List
from numpy import sort


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        nums = sorted(nums)

        ct=0
        prev=None
        for n in nums:
            if not prev or prev == n:
                prev = n
                ct+=1
                if ct > len(nums)/2:
                    return n
            else:
                prev =n
                ct=1

g = Solution()

print(g.majorityElement([2,2,1,1,1,2,2]))