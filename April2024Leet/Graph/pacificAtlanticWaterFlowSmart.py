from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        reachPacific = set()
        reachAtlantic = set()

        gridHeight = len(heights)
        gridLength = len(heights[0])

        for i in range(gridLength):
            ##Up
            self.dfs(0, i, heights, heights[0][i], reachPacific)
            ##Down
            self.dfs(gridHeight-1, i, heights, heights[gridHeight-1][i], reachAtlantic)

        for i in range(gridHeight):
            self.dfs(i, 0, heights, heights[i][0], reachPacific)
            self.dfs(i, gridLength-1, heights, heights[i][gridLength-1], reachAtlantic)

        ans = []

        for coord in reachPacific:
            if coord in reachAtlantic:
                ans.append([coord[0],coord[1]])

        return ans

    def dfs(self, x, y, grid, prevHeight, ansSet):

        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in ansSet or grid[x][y]<prevHeight:
            return
        ansSet.add((x, y))
        height = grid[x][y]

        self.dfs(x+1, y, grid, height, ansSet)
        self.dfs(x-1, y, grid, height, ansSet)
        self.dfs(x, y-1, grid, height, ansSet)
        self.dfs(x, y+1, grid, height, ansSet)

sol = Solution()
print(sol.pacificAtlantic([[1,1],[1,1],[1,1]]))
