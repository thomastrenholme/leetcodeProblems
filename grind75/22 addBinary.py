class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        c=[]
        
        aCtr=len(a)-1
        bCtr=len(b)-1

        carry=0
        while aCtr>=0 or bCtr>=0 or carry>0:

            if aCtr>=0 and bCtr>=0:
                val = (int(a[aCtr]) + int(b[bCtr]) + carry)
            elif aCtr>=0:
                val = (int(a[aCtr]) + carry)
            elif bCtr>=0:
                val = (int(b[bCtr]) + carry)
            else:
                ##carry only
                val = carry
            if val==0 or val==2:
                c.append("0")
            else:
                c.append("1")
            carry = 1 if val>=2 else 0
            aCtr-=1
            bCtr-=1
            
        ret=""
        while c:
            ret+=(c.pop())
        return ret

g = Solution()
print(g.addBinary("1010", "1011"))
