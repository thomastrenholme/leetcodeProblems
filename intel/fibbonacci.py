

def getFibbonaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return getFibbonaci(n-1)+getFibbonaci(n-2)

print(getFibbonaci(10))





def sumOfFirstNFibbonaci(n):
    res = 0

    for i in range(0, n):
        res += getFibbonaci(i)
    return res

print(sumOfFirstNFibbonaci(10))