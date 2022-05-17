# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    pairsCtr = 0
    dictOfArr = {}
    for i in arr:
        dictOfArr[i] = 1

    
    for i in arr:
        if dictOfArr.get(i-k) is not None:
            pairsCtr+=1