class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ##find pivot index

        pivot = self.findPivot(nums, 0, len(nums))


        if not pivot:
            pivot= 0

        print("pivot: " + str(pivot))
        
        ##then use arr splicing to make fixed arr
        newArr = nums[pivot:len(nums)]+nums[0:pivot]

        print("newArr:" + str(newArr))
        ##then bin search it
        ans = self.binSearch(newArr, target)

        print("Ans:"  + str(ans))

        return ans if ans == -1 else ans + pivot

    def findPivot(self, nums, l, r):
        
        middle = (l + r) // 2
        while l <= r:
            
            print("l: " + str(l) + " r: " + str(r))
            print("middle: " + str(middle))
            ##Wrap around array for comparison if necessary
            if nums[middle % len(nums)] < nums[(middle+1) % len(nums)]:
                return (middle-1) % len(nums)
            elif nums[middle % len(nums)] < nums[l % len(nums)]:
                ##pivot is somewhere in l-middle
                return self.findPivot(nums, l, middle-1)
            else:
                return self.findPivot(nums, middle+1, r)

    def binSearch(self, arr, target):
        l = 0
        r=len(arr)-1

        middle = (l+r) // 2

        while l <= r:
            middle = (l+r) // 2

            if arr[middle] == target:
                return middle
            elif arr[middle] < target:
                l = middle+1
            else:
                r = middle-1
        return -1
    


g = Solution()
print(g.search([1, 3], 1))



