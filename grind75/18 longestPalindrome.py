class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        oddLetters = set()

        for l in s:
            if l not in oddLetters:
                oddLetters.add(l)
            else:
                oddLetters.remove(l)
            
        return len(s) - len(oddLetters) +1 if len(oddLetters) > 0 else len(s)

g = Solution()
print(g.longestPalindrome("abccccdd"))
        