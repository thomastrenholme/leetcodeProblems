from collections import defaultdict
import sys
from typing import List


class Solution:

    ##This is DFS, I will do the BFS later
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        nRows=len(grid)
        nCols=len(grid[0])

        ##Initial time for all oranges is infinity, we will check when DFSing to them if currtime is less than this time.
        ##Else, just return from unnecessary DFS.
        orangeClock=defaultdict(lambda: sys.maxsize)
        ##False is now rotten, true is fresh orange
        freshCount=0
        freshMap={}

        def rotFirstSearch(i, j, currTime, orangeClock):

            ##Has to be in bounds, not empty cell, and currTime has to be less than prev updated time
            if 0<=i<nRows and 0<=j<nCols and grid[i][j] != 0 and orangeClock[(i, j)] > currTime:
                
                print("Curr cell: " + str( (i, j)))
                print("Curr time: " + str(currTime))
                ##Add to freshOrangeMap that it turned into rotten orange, if previously was fresh
                if grid[i][j] == 1 and (i, j) not in freshMap:
                    nonlocal freshCount
                    freshCount-=1
                    freshMap[(i, j)] = True

                orangeClock[(i, j)] = currTime

                ##DFS to neighbors
                
                rotFirstSearch(i+1, j, currTime+1, orangeClock)
                rotFirstSearch(i-1, j, currTime+1, orangeClock)
                rotFirstSearch(i, j+1, currTime+1, orangeClock)
                rotFirstSearch(i, j-1, currTime+1, orangeClock)

        for i in range(nRows):

            for j in range(nCols):
                
                ##If fresh orange, and hasnt been catalogued already, set it to Fresh in the dict.
                if grid[i][j]==1:
                    freshCount+=1
                
                ##DFS from rotten oranges only
                if grid[i][j]==2:
                    rotFirstSearch(i, j, 0, orangeClock)
        
        ##If still any fresh oranges, return false
        if freshCount > 0:
            return -1
        return max(orangeClock.values()) if len(orangeClock) > 0 else 0

g = Solution()
print(g.orangesRotting(
[[2,1,1],[0,1,1],[1,0,1]]))