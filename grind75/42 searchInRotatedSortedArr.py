class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l=0
        r = len(nums)-1

        while l<r:
            m = l + (r-l)//2
            print("M:" + str(m))
            print("L: " + str(l))
            print("r: " + str(r))

            ##Pivot must be to the right
            if nums[m] > nums[r]:
                l = m+1
            ##Pivot must be to the left
            else:
                r = m
        
        ##l idx will be smallest element in the arr
        print(l)
        def binSearch(l, r, target, arr):
            while l<=r:
                print("L: " + str(l))
                print("r: " + str(r))
                middle= l + (r-l)//2

                if arr[middle] > target:
                    r = middle-1
                elif arr[middle] < target:
                    l = middle+1
                else:
                    return middle
            return -1

        if nums[l]<=target<=nums[len(nums)-1]:
            return binSearch(l, len(nums)-1, target, nums)       
        else:
            return binSearch(0, l, target, nums)
            
        
        

g = Solution()
print(g.search([5,1,3], 1))