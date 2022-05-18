
import copy
from unicodedata import digit


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        

        myLetterDict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        letterToNumDict = {"a": "2", "b": "2", "c": "2", "d": "3", "e": "3", "f"}
        # if len(digits)==1:
        #     return myLetterDict[digits]
        # res = []
        # ctr=0
        # for dig in digits:

        #     print(str(myLetterDict[dig]))
        #     for let in myLetterDict[dig]:
        #         ##print("let: " + let)

        #         if ctr+1==len(digits):
        #             break
        #         for otherDigit in digits[ctr+1:]:

        #             for otherLetter in myLetterDict[otherDigit]:

        #                 res.append(let+otherLetter)
                
        #     ctr+=1
        # return res

        strOfAllLetters=""
        for dig in digits:
            strOfAllLetters+= (let for let in myLetterDict[dig])
        
        uniqueLetters=set(strOfAllLetters)
        
        copyUnique=copy(uniqueLetters)
        resStr=""
        for letter in uniqueLetters:

            while len(copyUnique) >=1:
                if copyUnique.pop() in myLetterDict[]
            
        


g = Solution()

print(g.letterCombinations("234"))