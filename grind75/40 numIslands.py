
from typing import List


class Solution:
    nIslands=0
    def numIslands(self, grid: List[List[str]]) -> int:
        
        nRows = len(grid)
        nCols = len(grid[0])

        

        def dfsIslands(i, j, visited, parent=False):

            if 0<=i<=nRows-1 and 0<=j<=nCols-1 and (i, j) not in visited and grid[i][j] != "0":
                ##were on land
                visited.add((i, j))
                dfsIslands(i + 1, j, visited)
                dfsIslands(i - 1, j, visited)
                dfsIslands(i, j+1, visited)
                dfsIslands(i, j-1, visited)

                if parent:
                    self.nIslands+=1

        visited=set()
        for i in range(nRows):
            for j in range(nCols):
                dfsIslands(i, j, visited, parent=True)

        return self.nIslands


g = Solution()
print(g.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))