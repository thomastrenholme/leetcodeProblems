class Solution:
    def longestPalindrome(self, s: str) -> int:
        

        letterDict = {}

        for l in s:

            if l in letterDict:
                letterDict[l] += 1
            else:
                letterDict[l] =1

        longestLen=0

        oneUsed = False
        for key in letterDict:
            if letterDict[key]==1 and not oneUsed:
                oneUsed=True
                longestLen+=1
            while letterDict[key] >= 2:
                letterDict[key]-=2
                longestLen+=2

        return longestLen

g = Solution()
print(g.longestPalindrome("abccccdd"))
        