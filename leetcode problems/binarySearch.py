from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:


        def bSearch(arr, target):

            l = 0
            r = len(arr)-1

            middle = l + (r-l)//2

            while l <= r:
                middle = l + (r-l)//2

                if target > arr[middle]:
                    l = middle +1
                elif target < arr[middle]:
                    r = middle -1
                else:
                    return middle
            return -1

                    
        return bSearch(nums, target)
