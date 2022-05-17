from hashlib import new


a = {2: " dwdw", 1: "dwdw"}


print(str(a))




class Poop:

    def getIntInRow(self, row, index):
        if(index < 0 or index >= len(row)):
            return 0
        return row[index]

    def getNthRowPascals(self, n):
        row = [1]
        for i in range (0, n):
            newRow = []

            for j in range(0, i+2):
                newRow.append(self.getIntInRow(row, j -1) + self.getIntInRow(row, j))
            
            print("new row: " + str(newRow))
            row = newRow

        return row
        


g = Poop()
print(str(g.getNthRowPascals(7)))



g = [2]
print(str(g[-1]))