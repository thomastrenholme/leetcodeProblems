
from gettext import install


def superDigit(n, k):
    # Write your code here
    sd = sumDigitInStr(n)

    return sup_dig(str(int(sd) * k))

def sup_dig(str):
    if len(str) <= 1:
        return str
    return sup_dig( sumDigitInStr(str))

def sumDigitInStr(inputStr):
    return str(sum( (int(i) for i in list(inputStr))) )


print(superDigit("123", 3))
