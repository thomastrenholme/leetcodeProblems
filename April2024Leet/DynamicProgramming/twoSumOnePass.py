

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        numsToIndicies = {}

        for i in range(len(nums)):
            n = nums[i]
            targetVal = target - n

            if targetVal in numsToIndicies:
                return [numsToIndicies[targetVal], i]
            else:
                numsToIndicies[n] = i