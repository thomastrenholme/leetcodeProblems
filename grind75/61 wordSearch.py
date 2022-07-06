from typing import List


class Solution:
    wordFound=False
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        nRows, nCols = len(board), len(board[0])

        def dfs(i, j, index, word, visited):

            if self.wordFound:
                return True
            if 0<= i < nRows and 0<= j < nCols and (i, j) not in visited and board[i][j] == word[index]:
                ##letter found, now DFS to neighbors
                visited.add((i,j))
                index+=1
                if index==len(word):
                    self.wordFound=True
                    return True
                
                if dfs(i+1, j, index, word, visited) or dfs(i-1, j, index, word, visited) or dfs(i, j+1, index, word, visited) or dfs(i, j-1, index, word, visited):
                    self.wordFound==True
                    return True
                else:
                    visited.remove((i, j))
            
            return False

        
        for i in range(nRows):

            for j in range(nCols):
                if dfs(i, j, 0, word, set()):
                    return True
        return False

                
g = Solution()
print(g.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))