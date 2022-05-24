from math import floor


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        n=0
        for l in s:
            if l == letter:
                n+=1

        return floor(float(n)/len(s) * 100)

