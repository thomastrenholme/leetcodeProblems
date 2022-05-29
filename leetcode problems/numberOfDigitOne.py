class Solution:
    def countDigitOne(self, n: int) -> int:
        
        res = 0
        
        tensPlaceCtr=0

        ctr=0

        
        while n-1000>ctr:
            res+=301
            ctr+=1000
        
        for i in range(ctr, n+1):

            if '1' in str(i):

                for j in str(i):

                    if j=='1':
                        res+=1

        
            
        return res

g = Solution()

print(g.countDigitOne(89200))