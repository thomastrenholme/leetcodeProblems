
import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    ##lonely is odd so n/2 runtime
    a.sort()
    i = 0
    while(i < len(a)):
        if not (i+1) >= len(a) and a[i+1] != a[i]:
            ##lonely
            return a[i]
        i+=2##skip next one cause its the same 

    ##reached end, return last val
    return a[len(a)-1]

b = "59 88 14 8 85 1 94 74 57 96 39 2 47 43 35 17 53 52 92 31 99 48 94 30 92 60 32 45 88 13 39 50 22 65 89 46 65 76 57 67 99 35 76 46 85 82 45 62 53 80 74 22 31 52 82 13 41 96 2 1 80 62 4 20 50 89 59 67 60 8 41 14 47 48 17 4 43 30 32"
c = b.split()
a = [int(num) for num in c]
print(lonelyinteger(a))





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
