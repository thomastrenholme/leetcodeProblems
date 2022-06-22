from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        retArr=[1]*len(nums)
        productOfEverything = 1
        zeroPresent=False
        

        for i in nums:
            if i != 0:
                ##Non-zero number, add to the product total
                productOfEverything*= i

            elif i==0 and zeroPresent:
                ##If second zero, everything in arr will be 0
                return [0]*len(nums)
            else:
                ##First zero appearance
                zeroPresent = True
        
        for i in range(len(nums)):
            if zeroPresent and nums[i] != 0:
                retArr[i]=0
            elif zeroPresent:
                ##nums[i] is zero and we just take product of everything else
                retArr[i]=productOfEverything
            else: 
                ##No zeros, normal behavior
                retArr[i]= int(productOfEverything * nums[i]**-1)
        return retArr

    ##My way above, actual smart way below
    def productExceptSelf2(self, nums: List[int]) -> List[int]:

        ans = [1 for _ in nums]

        left = 1
        right = 1

        for i in range(len(nums) -1):
            ans[i]*=left
            ans[-1-i]*=right
            left *=nums[i]
            right *=nums[-1-i]
        return ans
            




g = Solution()
print(g.productExceptSelf([-1,1,0,-3,3,0]))