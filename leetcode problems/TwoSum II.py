from typing import List
##https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers)-1
        
        while True:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                r-=1

g = Solution()

print(g.twoSum([2, 7, 11, 15], 9))