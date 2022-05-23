import copy
from re import T


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
    
        res = []

        
        def helperFunc(arr, nums):
            # print("Curr arr: " + str(arr) + " curr nums: " + str(nums))
            if len(nums) == 0:
                res.append(arr)

            for n in nums:
                tmpNums = copy.copy(nums)
                tmpArr = copy.copy(arr)
                tmpArr.append(n)
                tmpNums.remove(n)
                helperFunc(tmpArr, tmpNums)

        helperFunc([], nums)
        
        return res

g = Solution()

print(g.permute([0, 1]))
