class Solution:
    largestGroupOfBlocks = 0
    def findLargestGroupOfColors(self, color: list[list[int]]):


        def bfs(i, j, visited, colorOfBlock, numOfLikeColorBlocks):
            
            
            if 0 <= i <= len(color)-1 and 0 <= j <= len(color[0])-1 and (i, j) not in visited and color[i][j] == colorOfBlock:

                visited.add( (i, j) )
                numOfLikeColorBlocks+=1
                self.largestGroupOfBlocks= max(self.largestGroupOfBlocks, numOfLikeColorBlocks)

                bfs(i +1, j, visited, colorOfBlock, numOfLikeColorBlocks)
                bfs(i -1, j, visited, colorOfBlock, numOfLikeColorBlocks)
                bfs(i, j+1, visited, colorOfBlock, numOfLikeColorBlocks)
                bfs(i, j-1, visited, colorOfBlock, numOfLikeColorBlocks)

        for i in range(0, len(color)):

            for j in range(0, len(color[0])):
                visited=set()
                bfs(i, j, visited, color[i][j], 0)
        return self.largestGroupOfBlocks

g = Solution()
print(g.findLargestGroupOfColors([ [1,1,1,1,1],[2,2,1,1,2],[3,4,3,4,3] ]))
        
##https://www.geeksforgeeks.org/largest-connected-component-on-a-grid/