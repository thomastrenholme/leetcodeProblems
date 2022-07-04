
class Solution:
    def longestPalindrome(self, s: str) -> str:

        retPalindrome=""

        def checkForPalindrome(l, r, s):
            while 0<= l and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1

            return s[l+1:r]
        
        
        
        for idx, char in enumerate(s):
            retPalindrome = max(checkForPalindrome(idx, idx, s), checkForPalindrome(idx, idx+1, s), retPalindrome, key=len)

        return retPalindrome


g = Solution()
print(g.longestPalindrome("abb"))