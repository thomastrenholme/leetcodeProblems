from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        badIdxs= []
        endCtr = len(nums) -1

        for i in range(0, len(nums)):

            if i == val and endCtr > i:
                while(endCtr == val):
                    endCtr -= 1
                nums[i] = nums[endCtr]
                badIdxs.append(endCtr)
                endCtr -= 1
            elif i != val and endCtr < i:
                lowestIdx = badIdxs.pop()
                nums[lowestIdx] = nums[i]
                endCtr+=1
        
        print(nums)
        return endCtr




g = Solution()

print(g.removeElement([0,1,2,2,3,0,4,2], 2))