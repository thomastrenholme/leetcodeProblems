class Solution:
    def isValid(self, s: str) -> bool:
        parStack = []

        openDict = {"}": "{", "]": "[", ")": "("}

        for p in s:

            if p not in openDict:
                parStack.append(p)

            else:
                if not parStack:
                    return False
                oPar = parStack.pop()

                if openDict[p] != oPar:
                    return False

        if not parStack:
            return True
        return False
g = Solution()

print(g.isValid("[()]"))