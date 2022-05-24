from sqlite3 import TimestampFromTicks
from tempfile import tempdir


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        idxCtr=1
        sum = 0
        nCtr=0
        tensPlaceCtr=0
        carry = 0
        for n in num1[::-1]:

            for n2 in num2[::-1]:

                print("n: " + n + " n2: " + n2)

                if idxCtr==len(num2):
                    sum+= (int(n) * int(n2) + carry) * (10**tensPlaceCtr)

                else:

                    tmpSum = (int(n) * int(n2) + carry)

                    carry = tmpSum // 10

                    print("temp sum: " + str(tmpSum) + " carry: " + str(carry))

                    sum+= tmpSum % 10  * (10**tensPlaceCtr)
                    tensPlaceCtr+=1
                    idxCtr+=1
            print("Sum is "  + str(sum))
            print("\n\nend\n\n")


                
                ##print("Sum is: " + str(sum))
            carry = 0
            idxCtr=1
            nCtr+=1
            tensPlaceCtr= 0+nCtr

        return sum
g = Solution()

print(g.multiply("5678", "1234"))