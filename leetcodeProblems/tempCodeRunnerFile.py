
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        

        ##given n pairs generate all combos of well formed parenthesis

        res = []

        def helperFunc(oCtr, cCtr, tmpStr):
            
            ##if openCtr still has parenthesis, add
            if oCtr:
                helperFunc(oCtr-1, cCtr, tmpStr+"(")

            if cCtr > oCtr:
                helperFunc(oCtr, cCtr-1, tmpStr+")")
            
            ##All pairs put, return tmpStr
            if not cCtr:
                res.append(tmpStr)
                return
            

            
            
        helperFunc(n, n, "")
        return res

g = Solution()
print(g.generateParenthesis(5))

        