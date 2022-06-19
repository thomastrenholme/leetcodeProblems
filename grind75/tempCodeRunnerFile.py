from re import T
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        ##go through list of tokens, if no operation between numbers, assume parenthesis
        ##maybe use stack

        opDict = ["*", "/", "+"]
        numDict = []
        ##num num operation
        stack = []
        tokensIdxCtr=0
        ##while still operations or nums
        while tokensIdxCtr<len(tokens):

            while tokens[tokensIdxCtr].lstrip("-").isdigit():
                stack.append(int(tokens[tokensIdxCtr]))
                tokensIdxCtr+=1
            ##isnt digit. num1 op num2
            ##is op
            operator = tokens[tokensIdxCtr]
            tokensIdxCtr+=1
            num2 = stack.pop()
            num1 = stack.pop()
            newNum=0
            if operator=="+":
                newNum = num1+num2
            elif operator=="*":
                newNum=num1*num2
            else:
                newNum=int(num1/num2)
            stack.append(newNum)
            print("tokens")
            print(tokens[tokensIdxCtr:])
            print(stack)
        return stack[0]

g = Solution()
print(g.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
            



            