# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq


def cookies(k, A):
    # Write your code here

    interationsRequired = 0

    ##minHeap approach
    cookieMinHeap = A

    heapq.heapify(cookieMinHeap)

    ##while less than min sweetness
    while cookieMinHeap[0] < k:
        newCookie1 = heapq.heappop(cookieMinHeap)
        if not len(cookieMinHeap) > 0:
            return -1
        newCookie2 = heapq.heappop(cookieMinHeap)

        combinedCookie = (newCookie1 + 2*newCookie2)

        heapq.heappush(cookieMinHeap, combinedCookie)
        interationsRequired+=1

    return interationsRequired