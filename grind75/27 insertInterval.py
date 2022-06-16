from hashlib import new
from os import TMP_MAX
from re import I
from typing import List


class Solution:
    def insert(self, intervals, I):
        res, i = [], -1
        for i, (x, y) in enumerate(intervals):
            if y < I[0]:
                res.append([x, y])
            elif I[1] < x:
                i -= 1
                break
            else:
                I[0] = min(I[0], x)
                I[1] = max(I[1], y)
                
        return res + [I] + intervals[i+1:]


g = Solution()

print(g.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))