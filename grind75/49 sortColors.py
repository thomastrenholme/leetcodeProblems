import math
import random
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redIdx, whiteIdx, blueIdx = 0, 0, len(nums) -1

        while whiteIdx <= blueIdx:
            if nums[whiteIdx] == 0:
                nums[redIdx], nums[whiteIdx] = nums[whiteIdx], nums[redIdx]
                redIdx+=1
                whiteIdx+=1
            
            elif nums[whiteIdx] == 2:
                nums[blueIdx], nums[whiteIdx] = nums[whiteIdx], nums[blueIdx]
                blueIdx-=1
            else:
                ##nums[whiteIdx] == 1 (white)
                whiteIdx+=1
        return nums


g = Solution()
print(g.sortColors(nums = [2,0,2,1,1,0]))