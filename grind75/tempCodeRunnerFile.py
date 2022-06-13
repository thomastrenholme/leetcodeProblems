##https://leetcode.com/problems/climbing-stairs/

from collections import defaultdict
from tkinter import NS


class Solution:
    nStairsToUniqueWays = {}
    numUniqueWays = 0
    
    ##The fibbonacci number of n is made up of (n-2) + (n-1) so that will be the number of ways
    def fib(self, n):
        if n<=2:
            return 1
        fibCtr=2

        a=1
        b=1
        while fibCtr< n:
            c=a+b
            a=b
            b=c
            fibCtr+=1
        return c



g = Solution()

print(g.fib(20))
# print(g.climbStairs(3))