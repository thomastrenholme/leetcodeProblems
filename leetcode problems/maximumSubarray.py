import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        currSum=0
        maxSum=0

        for n in nums:

            currSum = max(n, n+currSum)
            maxSum = max(currSum, maxSum)