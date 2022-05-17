class Solution:
    def mySqrt(self, x: int) -> int:
        
        return self.binSearch(x)
    
    def binSearch(self, x):
        l = 0
        r = x
        
        while l <= r:

            mid = (l+r) //2

            ##print("L is: " + str(l) + " R is: " + str(r) + " MID IS: " + str(mid))
            
            if mid*mid <= x < (mid+1) * (mid+1):
                return mid

            elif mid*mid > x:
                r = mid-1
            
            else:
                l = mid+1
        return mid

g = Solution()

print(g.mySqrt(8503128))