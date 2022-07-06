import copy


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        myLetterDict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], 
        "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], 
        "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        if len(digits) == 0:
            return []
        
        res = []

        ##Put the first letters
        currNum = digits[0]
        for let in myLetterDict[currNum]:
            res.append(let)

        ##Append all combos
        ctr=1
        while ctr < len(digits):
            currNum = digits[ctr]
            ##Make a new res var every round that will hold the letter combos of len(ctr), 
            # go through all letters of the newly selected current num
            ##and append them to all the current combos
            newRes=[]
            for let in myLetterDict[currNum]:
                for letCombo in res:
                    newRes.append(letCombo+ let)
            res=newRes
            ctr+=1
        
        ##return only the correct len combos
        return newRes

g = Solution()
print(g.letterCombinations("234"))
