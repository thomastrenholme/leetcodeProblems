from datetime import datetime
from matplotlib.pyplot import grid


def gridTravel(m, n): 
    numWays=0
    def dfs(i, j):
        if 0<=i<=m-1 and 0<=j<=n-1:

            if i==m-1 and j==n-1:
                nonlocal numWays 
                numWays+=1
                return
            
            dfs(i+1, j)
            dfs(i, j+1)
      
    dfs(0, 0)
    return numWays

print(datetime.now())
print(gridTravel(15, 15)) 
print(datetime.now())


def gridTravel2(m ,n, memo = {}):

    if (m, n) in memo: return memo[(m, n)]

    if m==0 or n==0:
        return 0
    if m<=1 or n<=1:
        return 1
    memo[(m, n)] = gridTravel2(m - 1, n, memo) + gridTravel2(m, n-1, memo)
    return memo[(m, n)]


print("#2: \n\n")
print(datetime.now())
print(gridTravel2(15, 15))
print(datetime.now())

        