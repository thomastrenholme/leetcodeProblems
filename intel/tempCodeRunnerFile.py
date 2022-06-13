

class fib:

    def smartGetFib(self, n):
        a = 0
        b = 1
        c = 0

        i = 0
        while i < n:
            c = a+b
            tmp = a
            a = c 
            b = tmp
            i+=1
        return c
        

    def getFibbonaci(self, n, fibMap, origValue=None):
        if not origValue:
            origValue=n
        if n==0:
            return 0
            
        elif n==1:
            return 1
        else:
            if n in fibMap:
                return fibMap[n]
            else:
                return getFibbonaci(n-1)+getFibbonaci(n-2)

g = fib()
print(g.smartGetFib(10))





# def sumOfFirstNFibbonaci(n):
#     res = 0

#     for i in range(0, n):
#         res += getFibbonaci(i)
#     return res

# print(sumOfFirstNFibbonaci(10))