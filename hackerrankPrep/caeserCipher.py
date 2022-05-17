#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    aDict = {}
    aDictCtr=0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        aDict[letter] = aDictCtr
        aDictCtr+=1

    newStr=""
    cap = False
    print("S: " + s)
    for letter in s:
        if letter.isupper():
                cap = True
        if letter.lower() in aDict.keys():
            tmp = ""
            ##shift
            idx = aDict[letter.lower()]
            tmp = alphabet[(idx + k)%26]

            print("old letter: " + letter + " new letter: " + tmp)
        else:
            tmp = letter
        if cap:
            tmp = tmp.capitalize()
            cap = False
        newStr+=tmp

    return newStr


print(caesarCipher("middle-Outz", 2))