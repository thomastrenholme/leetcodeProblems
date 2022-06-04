from cgitb import small

from pandas import pivot


class Solution:
    def search(self, nums: list[int], target: int) -> int:


        if not nums or len(nums) == 0: return -1

        smallestElementIdx = self.findPivot(nums)

        left = 0
        right = len(nums)-1
        
        if target >= nums[smallestElementIdx] and target <= nums[len(nums)-1]:
            left = smallestElementIdx
        else:
            right = smallestElementIdx

        print("left: " + str(left) + "right: " + str(right))
        
        return self.binSearch(target, nums, left, right)

    def binSearch(self, target, nums, left, right):
        l = left
        r = right

        while l <= r:
            m = l + int((r - l)/2)

            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m
    def findPivot(self, nums):
        l = 0
        r = len(nums) -1
        middle = 0

        while l < r:
            middle = l + int((r - l) /2)
            
            ##if middle greater than right, set left boundary to middle. smallest element is between pivot and right
            if nums[middle] > nums[r]:
                l = middle +1
            
            ##pivot is between middle and left (inclusive)
            else:
                r = middle
        return l


g = Solution()

print(g.search([4,5,6,7,0,1,2], 0))