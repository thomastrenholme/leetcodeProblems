
class Solution:

    def __init__(self):
        self.visited = set()
        self.n = 0
    def numIslands(self, grid: list[list[str]]) -> int:

        length = len(grid)
        height = len(grid[0])

        for i in range(0, length):

            for j in range(0, height):

                self.checkIsland(i, j, grid, True)

        return self.n

    def checkIsland(self, x:int, y:int, grid: list[list[str]], parent: bool):

        gridLength = len(grid)
        gridHeight = len(grid[0])

        if 0 <= x < gridLength and 0 <= y < gridHeight and grid[x][y] == "1" and not (x, y) in self.visited:

            if parent:
                self.n += 1

            self.visited.add((x, y))

            self.checkIsland(x+1, y, grid, False)
            self.checkIsland(x-1, y, grid, False)
            self.checkIsland(x, y+1, grid, False)
            self.checkIsland(x, y-1, grid, False)




