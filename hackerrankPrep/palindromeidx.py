#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

##if already palindrome or impossible, return negative one

def palindromeIndex(s):
    # Write your code here
    if len(s) <= 2 or s[::-1] == s:
        return -1
    
    idx = 0
    for letter in s:

        ##end of word idx
        if idx == len(s) - 1:

            tmpS = s[:idx]
            if tmpS == tmpS[::-1]:
                return idx
            return -1
        
        tmpSfront = s[:idx]
        tmpSend = s[idx+1:]

        tmpFullStr = tmpSfront + tmpSend

        if tmpFullStr == tmpFullStr[::-1]:
            return idx
        idx+=1