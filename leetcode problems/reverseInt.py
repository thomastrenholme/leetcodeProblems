class Solution:
    def reverse(self, x: int) -> int:
        
        intStr = str(x)

        newX = ""
        pos=True
        if(intStr[0]=='-'):
            pos=False
            intStr = intStr[1:]


        for digit in intStr[::-1]:
            newX+=digit

        if not pos:
            newX = '-' + newX

        newIntx = int(newX)

        if newIntx < -2**31 or newIntx > 2**31 -1:
            return 0

        return newIntx