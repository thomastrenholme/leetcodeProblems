from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers)-1
        
        while True:
            if numbers[l] + numbers[r] == target:
                return [numbers[l], numbers[r]]
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                r-=1

g = Solution()

print(g.twoSum([2, 7, 11, 15], 9))