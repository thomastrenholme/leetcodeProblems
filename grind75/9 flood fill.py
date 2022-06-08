from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        nRows = len(image)
        nCols = len(image[0])

        visited = set()
        def dfs(i, j, currColor, newColor):

            if (i, j) not in visited and 0 <= i <= nRows-1 and 0<= j <= nCols-1 and image[i][j] == currColor:

                visited.add(i, j)
                image[i][j] = newColor
                dfs(i +1, j, currColor, newColor)
                dfs(i -1, j, currColor, newColor)
                dfs(i, j+1, currColor, newColor)
                dfs(i, j-1, currColor, newColor)
        dfs(sr, sc, image[sr][sc], newColor)


g = Solution()
print(g.floodFill([[0,0,0],[0,0,0]], 0, 0, 2))