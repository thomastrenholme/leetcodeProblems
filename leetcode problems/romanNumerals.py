class Solution:
    def romanToInt(self, s: str) -> int:
        
        total=0
        sCtr=0
        while sCtr <= len(s)-1:
            addToTot=self.convert(s[sCtr])
            if self.subtractConvert(s[]
    
    def convert(self, s):
        if s=="M":
            return 1000
        elif s=="D":
            return 500
        elif s=="c":
            return 100
        elif s=="L":
            return 50
        elif s=="X":
            return 10
        elif s=="V":
            return 5
        elif s=="I":
            return 1
    
    def subtractConvert(self, s):
        if s=="CM":
            return 900
        elif s=="CD":
            return 400
        elif s=="XC":
            return 90
        elif s=="XL":
            return 40
        elif s=="IX":
            return 9
        elif s=="IV":
            return 4
        return "-1"
            
    def intToRoman(self, num: int) -> str:

        strNum = str(num)

        ones = ""
        tens = ""
        hundreds = ""
        thousands = ""
        ##reverse
        ctr=0
        for n in strNum[::-1]:

            if ctr==0:
                if int(n)<=3:
                    for i in range(0, int(n)):
                        ones+="I"
                elif int(n)==4:
                    ones+="IV"
                elif int(n)==9:
                    ones+="IX"
                elif int(n) >= 5:
                    ones+="V"
                    for i in range(5, int(n)):
                        ones+="I"
            
            elif ctr==1:
                if int(n)<=3:
                    for i in range(0, int(n)):
                        tens+="X"
                elif int(n)==4:
                    tens+="XL"
                elif int(n)==9:
                    tens+="XC"
                elif int(n) >= 5:
                    tens+="L"
                    for i in range(5, int(n)):
                        tens+="X"
            
            elif ctr==2:
                if int(n)<=3:
                    for i in range(0, int(n)):
                        hundreds+="C"
                elif int(n)==4:
                    hundreds+="CD"
                elif int(n)==9:
                    hundreds+="CM"
                elif int(n) >= 5:
                    hundreds+="D"
                    for i in range(5, int(n)):
                        hundreds+="C"

            else:
                for i in range(0, int(n)):
                    thousands+="M"
            ctr+=1
        return thousands+hundreds+tens+ones

g=Solution()
print(g.intToRoman(3877))
            
            
            