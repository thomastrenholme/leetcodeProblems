##https://leetcode.com/problems/climbing-stairs/

from collections import defaultdict
from tkinter import NS


class Solution:
    nStairsToUniqueWays = {}
    numUniqueWays = 0
    def climbStairs(self, n: int) -> int:
        

        def climbDfs(currStep, numStepsToReachTop):
            if currStep>numStepsToReachTop:
                return
                
            if currStep in self.nStairsToUniqueWays:
                return self.nStairsToUniqueWays[currStep]

            if currStep==numStepsToReachTop:
                self.numUniqueWays+=1
                return

            climbDfs(currStep+1, numStepsToReachTop)
            climbDfs(currStep+2,  numStepsToReachTop)
        
        climbDfs(0, n)
        return self.numUniqueWays

g = Solution()

print(g.climbStairs(3))