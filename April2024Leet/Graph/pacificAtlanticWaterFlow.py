from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        length = len(heights)
        height = len(heights[0])

        ans = []

        for i in range(length):

            for j in range(height):

                visited = set()
                touching = self.getTouchesAtlanticPacific(i, j, heights)

                if self.dfs(i, j, heights, visited.copy(), heights[i][j], touching):
                    ans.append([i, j])

        return ans

    def dfs(self, x: int, y: int, grid, visited: set, prevHeight: int, touching: set):

        if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0])-1 or prevHeight < grid[x][y] or (x, y) in visited:
            return False

        visited.add((x, y))

        touching.update(self.getTouchesAtlanticPacific(x, y, grid))

        if len(touching) == 2:
            return True

        height = grid[x][y]

        touchLeft = self.dfs(x-1, y, grid, visited.copy(), height, touching)
        touchRight = self.dfs(x+1, y, grid, visited.copy(), height, touching)
        touchUp = self.dfs(x, y+1, grid, visited.copy(), height, touching)
        touchDown = self.dfs(x, y-1, grid, visited.copy(), height, touching)

        return touchLeft or touchRight or touchUp or touchDown

    def getTouchesAtlanticPacific(self, x, y, grid):
        touching = set()

        ## Pacific
        if (x == 0 or y == 0):
            touching.add("p")

        ## Atlantic
        if (y==len(grid[0])-1 or x == len(grid)-1):
            touching.add("a")
        return touching


sol = Solution()
print(sol.pacificAtlantic([[13],[4],[19],[10],[1],[11],[5],[17],[3],[10],[1],[0],[1],[4],[1],[3],[6],[13],[2],[16],[7],[6],[3],[1],[9],[9],[13],[10],[9],[10],[6],[2],[11],[17],[13],[0],[19],[7],[13],[3],[9],[2]]))
