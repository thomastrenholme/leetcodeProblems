from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hMap = {}

        for i in nums:
            if i in hMap:
                return True
            else:
                hMap[i]=True
        return False