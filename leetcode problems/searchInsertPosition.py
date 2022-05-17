class Solution:

    def searchInsert(self, nums: list[int], target: int) -> int:
        
        return  self.binSearch(nums, target)


    
    def binSearch(self, arr, x):

        l = 0
        r = len(arr) -1
        mid = -1

        while l <= r:
            mid = (l + r) // 2
            print("L is: " + str(l) + " r is: " + str(r))
            print("Mid is: " + str(mid))

            if arr[mid] == x:
                return mid

            elif x > arr[mid]:
                l = mid + 1

            else:
                r = mid -1
        
        if x > arr[mid]:
            return mid+1
        return mid

g = Solution()

print(g.searchInsert([1,3,5,6], 2))