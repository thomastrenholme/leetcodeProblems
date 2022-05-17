

from copy import deepcopy
import math
import os
import random
import re
import sys
from this import d

# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    grid2 = deepcopy(grid)
    rowCtr = 0
    for row in grid:
        dummy = sorted(row)
        grid2[rowCtr] = dummy
        rowCtr+=1
    
    keepComparingForCol = {}

    print(str(grid2))
    colI = 0
    for letter in range(len(row[0])):

        print("this row: " + row)
        
        
        i = 0
        j = len(grid) - 1
        tmpArr = [0] * len(grid)
        tmpArrCtr = 0
        ##Go through all cols
        while i <= j:
            print("Checking: " + str(i))
            tmpArr[tmpArrCtr] = grid2[i][colI]

            i+=1
            tmpArrCtr+=1

        ##After loop through cols
        print(str(tmpArr))
        if not tmpArr == sorted(tmpArr):
            return "NO"
        i=0
        tmpArrCtr=0

        colI+=1
    return "YES"

strTest = "abc hjk mpq rtv"
test = strTest.split()
print(gridChallenge(test))