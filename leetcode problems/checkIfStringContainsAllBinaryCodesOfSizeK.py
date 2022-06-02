
import copy


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        

        codes = []

        requiredCombos = 2**k

        for i in range(len(s)-k+1):

            tmp = s[i:i+k]

            if tmp not in codes:
                codes.add(tmp)
                requiredCombos-=1
                if requiredCombos==0:
                    return True
            
        return False

        

g = Solution()

print(g.hasAllCodes(s="00110110", k=15))