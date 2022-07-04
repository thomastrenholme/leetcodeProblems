

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    nRows,nCols = n, n

    obDict = {}
    totalSquares = 0

    directions = ["N","NE","NW","W","SW","S","SE","E"]

    print(nRows)
    print(nCols)

    for ob in obstacles:
        obDict[(ob[0]-1, ob[1]-1)] = True
    
    def expandInDirection(i, j, dir):
        print("i: " + str(i) + " j: " + str(j) + " dir: " + dir)
        if 0<=i<nRows and 0<=j<nCols and (i, j) not in obDict:
            nonlocal totalSquares
            totalSquares+=1

            newI, newJ = i, j
            if dir=="N":
                newI=i+1
                newJ=j
            elif dir=="NE":
                newI=i+1
                newJ=j+1
            elif dir=="NW":
                newI=i+1
                newJ=j-1
            elif dir=="W":
                newI=i
                newJ=j-1
            elif dir=="SW":
                newI=i-1
                newJ=j-1
            elif dir=="S":
                newI=i-1
                newJ=j
            elif dir=="SE":
                newI=i-1
                newJ=j+1
            elif dir=="E":
                newI=i
                newJ=j+1

            expandInDirection(newI, newJ, dir)
        
    for dir in directions:
        expandInDirection(r_q-1, c_q-1, dir)
    
    return totalSquares -8

if  __name__ == '__main__':
    print(queensAttack(4, 0, 4, 4, []))