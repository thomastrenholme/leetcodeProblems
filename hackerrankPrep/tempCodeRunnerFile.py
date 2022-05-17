
import math
import os
import random
import re
import sys

from numpy import mod

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def allSame(a, b=None, c=None, d=None):
    return (a==b==c==d)
def legoBlocks(n, m):
    # Write your code here
    blocks = [(1, 1), (1, 2), (1, 3), (1, 4)]

    height, width = n,m


    ##Figure out how many ways one row (width) can be divided
    validWays = 0
    for lego in blocks:

        if width == lego[1] and width % lego[1] == 0:
            validWays+=1
            print(str(lego) + " GOOD")

        for secondLego in blocks:
            if not(lego == secondLego) and width % (lego[1] + secondLego[1]) == 0:
                print("width: " + str(width) + ". lego[1] + secondLego[1] " + str((lego[1] + secondLego[1])))
                validWays+=1
                print(str(lego) + str(secondLego)+ " GOOD")

            for thirdLego in blocks:
                if not(lego == secondLego ==thirdLego) and not(lego==thirdLego) and not(lego==secondLego) and not(secondLego==thirdLego) and width % (lego[1] + secondLego[1] + thirdLego[1]) == 0:
                    validWays+=1
                    print("width: " + str(width) + ". lego[1] + secondLego[1] +thirdLego[1]" + str((lego[1] + secondLego[1] + thirdLego[1])))
                    print(str(lego) + str(secondLego) + str(thirdLego) + " GOOD")

                for fourthLego in blocks:

                    if not(lego == fourthLego) and not(secondLego == thirdLego) and not(lego==secondLego==thirdLego) and not(secondLego==thirdLego==fourthLego) and not(lego==thirdLego and secondLego==fourthLego) and not(lego == secondLego ==thirdLego==fourthLego) and width % (lego[1] + secondLego[1] + thirdLego[1] + fourthLego[1]) == 0:
                        validWays+=1

    ##raise to power of height
    validWays**= height
    ##return ans mod(10**9 + 7)

    return mod(validWays, 10**9+7)

print(legoBlocks(4, 4))
