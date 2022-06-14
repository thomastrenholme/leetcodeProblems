##https://leetcode.com/problems/climbing-stairs/

from collections import defaultdict
from tkinter import NS


class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=1
        for x in range(n):
            c=a+b
            a=b
            b=c
        return a

g = Solution()

print(g.fib(20))
# print(g.climbStairs(3))