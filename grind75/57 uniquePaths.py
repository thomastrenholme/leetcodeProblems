class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        nRows, nCols = m, n

        def dfs(i, j, memo={}):

            if 0<= i < nRows and 0<= j < nCols:
                
                if (i, j) in memo:
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = dfs(i, j+1, memo) + dfs(i +1, j, memo)
                    return memo[(i, j)]
            return 0
                
        return dfs(0, 0, {(m-1,n-1): 1})

g = Solution()
print(g.uniquePaths(3, 7))