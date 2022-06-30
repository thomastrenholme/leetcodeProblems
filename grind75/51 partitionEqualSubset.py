from typing import List


class Solution:
    valid=False
    def canPartition(self, nums: List[int]) -> bool:
        
        def dfsSubsetSum(arr, arrSum, totalSum, memo = {}):

            if self.valid:
                return True
            if arrSum == totalSum:
                self.valid = True
                memo[totalSum] = True
                return memo[totalSum]

            if totalSum in memo:
                return memo[totalSum]

            for n in range(len(arr)):

                newArr = arr[0:n]+arr[n+1:len(arr)]
                if dfsSubsetSum(newArr, arrSum-arr[n], totalSum+arr[n], memo):
                    ##print("new ARR: " + str(newArr))
                    memo[totalSum] = True
                    return memo[totalSum]
            memo[totalSum] = False
            return memo[totalSum]
        return dfsSubsetSum(nums, sum(nums), 0, {})

g = Solution()
print(g.canPartition([1,5,11,5]))
