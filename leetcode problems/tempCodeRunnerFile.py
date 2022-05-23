import copy


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        oldMatrix=copy.copy(matrix)
        for i in range(0, len(matrix)):

            for j in range(0, len(matrix)):

                print("i: " + str(i) + " j: " + str(j))

                matrix[i][j] = oldMatrix[i][len(matrix[j]) -1 - j]

        print(str(matrix))


g = Solution()

print (g.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))