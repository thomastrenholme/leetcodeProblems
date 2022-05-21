class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        oldRow = [1]


        for x in range(1, rowIndex+1):
            
            newRow = [1]*(x+1)

            for newIdx in range(1, len(newRow)-1):

                newRow[newIdx] = oldRow[newIdx -1] + oldRow[newIdx]
            oldRow=newRow

        return oldRow


    def generate(self, numRows: int) -> list[list[int]]:
        

        res = [[1]]


        for x in range(1, numRows):
            
            newRow = [1]*(x+1)

            for newIdx in range(1, len(newRow)-1):

                newRow[newIdx] = res[x-1][newIdx -1] + res[x-1][newIdx]
            res.append(newRow)

        return res

g = Solution()

print(g.getRow(3))
