
## https://leetcode.com/problems/max-area-of-island/
class Solution:

    def __init__(self):
        self.maxArea = 0
        self.visited = set()

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:


        for i in range(len(grid)):

            for j in range(len(grid[0])):

                islandArea = self.checkIslandArea(grid, i, j)

                if islandArea > self.maxArea:
                    self.maxArea = islandArea

        return self.maxArea

    def checkIslandArea(self, grid: list[list[int]], xCoord: int, yCoord: int):

        gridLen = len(grid)
        gridHeight = len(grid[0])

        ## If out of bounds or not island or already visited, stop
        if xCoord < 0 or xCoord >= gridLen or yCoord < 0 or yCoord >= gridHeight or (xCoord, yCoord) in self.visited:
            return 0

        self.visited.add( (xCoord, yCoord) )

        if grid[xCoord][yCoord] == 0:
            return 0


        areaOfIsland = 1

        areaOfIsland += self.checkIslandArea(grid, xCoord-1, yCoord)
        areaOfIsland += self.checkIslandArea(grid, xCoord+1, yCoord)
        areaOfIsland += self.checkIslandArea(grid, xCoord, yCoord-1)
        areaOfIsland += self.checkIslandArea(grid, xCoord, yCoord+1)

        return areaOfIsland

solution = Solution()
print(solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,0,0,0,0,0,0,1,1,0,0,0,0]]))