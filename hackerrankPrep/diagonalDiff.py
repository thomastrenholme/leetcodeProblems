def diagonalDifference(arr):
    # Write your code here
    firstDiag = 0
    secondDiag = 0

    ColumnCounter = 0
    for i in range(len(arr)):
        firstDiag+= arr[i][ColumnCounter]
        secondDiag+= arr[i][len(arr[i]) - 1 - ColumnCounter]
        ColumnCounter+=1

    print("First diag: " + str(firstDiag) + " second diag: " + str(secondDiag))

    return abs(firstDiag - secondDiag)
