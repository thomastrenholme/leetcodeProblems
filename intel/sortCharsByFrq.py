##https://leetcode.com/problems/sort-characters-by-frequency/


import re

from numpy import sort


class Solution:
    def frequencySort(self, s: str) -> str:
        
        charDict = {}

        for i in s:
            if i in charDict:
                charDict[i]+=i
            else:
                charDict[i]=i
        
        vals = sorted(charDict.values(), key=len, reverse=True)

        retString=""
        for v in vals:
            retString+=v
        return retString

g = Solution()
print(g.frequencySort("treat"))