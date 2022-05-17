class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        sCtr=0

        pCtr=0

        for let in p:
            
            if let is not "*" and let is not "?":

                if sCtr >= len(s) or s[sCtr] is not let:
                    return False
                sCtr+=1
                pCtr+=1

            elif let is "?":

                if sCtr < len(s):
                    sCtr+=1
                    pCtr+=1

            elif let is "*":

                if pCtr + 1 < len(s):
                    ##Still more letters in P
                    tmpLetter= p[pCtr+1]

                    if tmpLetter is
                else:
                    ##No more letters in P, * matches any S.
                    return True
    
    