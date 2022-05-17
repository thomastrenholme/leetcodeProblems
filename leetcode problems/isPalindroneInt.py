class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        strNum = str(x)

        stCtr=0
        endCtr=len(strNum)-1


        while stCtr < endCtr:   

            ##print(strNum[stCtr] + " " + strNum[endCtr])

            if strNum[stCtr] != strNum[endCtr]:
                return False
            stCtr+=1
            endCtr-=1
        
        return True

g = Solution()

print(g.isPalindrome(575))