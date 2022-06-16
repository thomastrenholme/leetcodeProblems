from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        nRows=len(mat)
        nCols=len(mat[0])
        ##for each cell, if 0, result is 0, else bfs to closest 0
        res = [ [10000]*nCols for i in range(nRows)]


        def bfsBinMatrix(i, j, visited):
            
            print("parent: " + str( (i, j)))
            q = deque()
            q.append( (i, j, 0) )
            while q:
                firstNode = q.popleft()
                if firstNode[2] >= 10000:
                    return
                print("checking: " + str(q))
                visited.add( (firstNode[0], firstNode[1]) )

                if mat[firstNode[0]][firstNode[1]] == 0:
                    return firstNode[2]
                else:
                    i = firstNode[0]
                    j = firstNode[1]
                    dist=firstNode[2]
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= x < nRows and 0 <= y < nCols and (x, y) not in visited:
                            q.append((x, y, dist+1))
                
            
        for i in range(nRows):

            for j in range(nCols):
                visited=set()
                res[i][j] = bfsBinMatrix(i, j, visited)
        return res
        
g = Solution()

print(g.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]))