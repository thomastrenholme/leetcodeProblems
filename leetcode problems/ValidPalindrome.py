import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        newS = re.sub(r'[^a-zA-Z0-9]', '', s)

        print("newS: " + newS)
        l = 0
        r = len(newS)-1

        while l <= r:
            if not newS[l] == newS[r]:
                return False

            l+=1
            r-=1

        return True

g = Solution()

print(g.isPalindrome("ab_a"))