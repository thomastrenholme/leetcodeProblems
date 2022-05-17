class Solution:
    def isValid(self, s: str) -> bool:
        parStack = []

        openDict = {"}": "{", "]": "[", ")": "("}

        for p in s:

            if p not in openDict:
                parStack.append(p)

            else:
                oPar = parStack.pop()

                if openDict[p] != oPar:
                    return False


g = Solution()

print(g.isValid("(((())))"))