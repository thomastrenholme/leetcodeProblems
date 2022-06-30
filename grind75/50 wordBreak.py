from typing import List


class Solution:
    good = False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfsWord(s, index, memo = {}):
            if self.good:
                return True
            if index in memo:
                return memo[index]
            
            for w in wordDict:
                
                sz = len(w)
                if s[index:index+sz] == w:

                    if index +sz== len(s):
                        self.good=True
                        memo[index] = True
                        return memo[index]

                    if dfsWord(s, index+sz, memo):
                        memo[index] = True
                        return memo[index]
            memo[index] = False
            return memo[index]
        
        return dfsWord(s, 0, {})
        

g = Solution()
print(g.wordBreak("cars", ["car","ca","rs"]))