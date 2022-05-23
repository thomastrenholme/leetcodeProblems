import copy
from re import T

from numpy import union1d


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        
        uniqueCheck = {}
            
        
        res = []

        
        def helperFunc(arr, nums):
            # print("Curr arr: " + str(arr) + " curr nums: " + str(nums))
            if len(nums) == 0:
                chck = 0
                ctr=0
                for x in arr:
                    chck+=x*10**ctr
                    ctr-=1
                if chck not in uniqueCheck:
                    uniqueCheck[chck] = True
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
