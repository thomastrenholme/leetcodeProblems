from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        nRows, nCols = len(matrix), len(matrix[0])
        numItems = nCols*nRows
        res = []
        visited =set()
        i, j = 0, 0


        while len(res) < numItems:
            ##Go right
            while j < nCols and (i, j) not in visited:
                visited.add((i, j))
                res.append(matrix[i][j])
                j+=1

            ##Subtract 1 from j to get valid col num
            ##Increment i to new unexplored row
            j-=1
            i+=1


            ##Go down
            while i < nRows and (i, j) not in visited:
                visited.add((i, j))
                res.append(matrix[i][j])
                i+=1
            
            ##decrement j to unexplored col val
            ##decrement i to val in range
            j-=1
            i-=1

            
            ##Go left
            while j >= 0 and (i, j) not in visited:
                visited.add((i, j))
                res.append(matrix[i][j])
                j-=1
            
            ##Subtract 1 from i to new unexplored val
            ##Increment j to valid in range val
            i-=1
            j+=1


            ##Go up
            while i >= 0 and (i, j) not in visited:
                visited.add((i, j))
                res.append(matrix[i][j])
                i-=1
            
            ##Increment i to val in range
            ##Increment j to new unexplored col
            i+=1
            j+=1

        return res
        

            
g = Solution()
print(g.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))