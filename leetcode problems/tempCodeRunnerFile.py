from ast import Str
import copy


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        

        ##(i, j) is the top (left) point to swap
        def swap(i, j):
            nRows = len(matrix)

            top = matrix[i][j] 
            right = matrix[j][nRows-1-i] 
            bottom = matrix[nRows-1-i][nRows-1-j] 
            left = matrix[nRows-1-j][i] 

            ##swap top and right
            matrix[j][nRows-1-i] = top

            ##swap right and bottom
            matrix[nRows-1-i][nRows-1-j] = right

            ##swap bottom and left
            matrix[nRows-1-j][i] = bottom

            ##swap left and top
            matrix[i][j] = left

        
        ##Rotate matrix[rowNum] and do it using (swaps) swaps
        def rotateRow(rowNum, swaps):
            for i in range(rowNum, swaps-1):
                swap(rowNum, i)
            if rowNum <= len(matrix) // 2 -1:
                rotateRow(rowNum+1, swaps-1)


        rotateRow(0, len(matrix))

        for row in matrix:
            print(row)

        # for row in matrix:
        #     print(row)


g = Solution()

##print(g.rotate([[1,2,3],[4,5,6],[7,8,9]]))
m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print (g.rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))