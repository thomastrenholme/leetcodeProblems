import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here

    if len(s) % 2 ==1:
        return "NO"

    bracketDict = {"{": "}", "[": "]", "(": ")"}

    stack=[]

    for i in s:

        if  i == "{" or i == "[" or i == "(":
            stack.append(i)

        else:
            if stack:
                bracket = stack.pop()

                if i != bracketDict[bracket]:
                    return "NO"

            else:
                return "NO"
            
        
        
    return "YES"

file = open(os.path.join(os.path.dirname(__file__), 'testCase.txt'), 'r')

Lines= file.readlines()

for line in Lines:
    print(isBalanced(line))
    
    