# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    topLeftSize = len(matrix)//2

    ##last idx of val in matrix (len - 1)
    n = len(matrix) - 1

    totalSum = 0
    ##get max element in all positions for top left corner

    ##all rows
    for i in range(topLeftSize):

        ##all cols
        for j in range(topLeftSize):
            totalSum += max(matrix[i][j], matrix[i][n - j], matrix[n - i][j], matrix[n - i][n - j])
            ##topLeftCorner[i][j]=maxElement

    return totalSum

matrix1 = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

print("                           Answer: " + str(flippingMatrix(matrix1)))