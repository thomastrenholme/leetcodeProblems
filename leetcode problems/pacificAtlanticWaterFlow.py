from collections import defaultdict
from email.policy import default
import string
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])

        pacificSet, atlanticSet = set(), set()

        def dfs(row, col, visitedSet, prevHeight):
            ##cant go to this neighbor
            if( (row, col) in visitedSet or row < 0 or col < 0 or row == rows or col ==cols or heights[row][col] < prevHeight):
                return
            visitedSet.add((row, col))
            dfs(row + 1, col, visitedSet, heights[row][col])
            dfs(row , col+1, visitedSet, heights[row][col])
            dfs(row-1, col, visitedSet, heights[row][col])
            dfs(row, col-1, visitedSet, heights[row][col])

        for c in range(cols):

            dfs(0, c, pacificSet, heights[0][c])
            dfs(rows-1, c, atlanticSet, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pacificSet, heights[r][0])
            dfs(r, cols-1, atlanticSet, heights[r][cols-1])
        return list(pacificSet.intersection(atlanticSet))

            



g = Solution()
print(g.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))