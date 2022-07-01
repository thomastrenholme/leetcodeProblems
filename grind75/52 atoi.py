class Solution:
    def myAtoi(self, s: str) -> int:
        stringVal="0"
        pos = True
        ctr=0
        s = s.lstrip()
        if len(s)==0:
            return 0

        if(s[ctr]) == "-":
            pos = False
            ctr+=1
        elif s[ctr] == "+":
            ctr+=1

        while ctr<len(s) and s[ctr].isdigit():
            stringVal+=s[ctr]
            ctr+=1
        
        retVal = int(stringVal)
        if not pos:
            retVal*=-1
            if retVal < -2**31:
                retVal = -2**31
        
        elif pos:
            if retVal>2**31-1:
                retVal = 2**31-1
        return retVal
        

            