import re


class Solution:
    def myAtoi(self, s: str) -> int:
        
        retString = s.lstrip()
        if(len(retString)==0):
            return 0


        pos = True
        if(retString[0] == "-"):
            pos = False
            retString =retString[1:]
        elif(retString[0] == "+"):
            retString =retString[1:]

        sumStr = "0"
        for digit in retString:
            if not digit.isdigit():
                break
            sumStr+=digit
        
        sum = int(sumStr)
        if not pos:
            if abs(sum) > 2**31: 
                sum=2**31
            return int(sumStr) * -1
        if sum > 2**31 -1:
            sum = 2**31 -1
        return sum



g = Solution()
s = "                 +4923      dpqwdqw                  "
print(g.myAtoi(s))