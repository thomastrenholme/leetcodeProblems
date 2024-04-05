

## Not a problem, just labbing a part of kClosestPointsToOrigin
class binaryInsert:

    def __init__(self):
        self.orderedArr = []
        self.uniqueValueHolder = set()

    def insert(self, valueToInsert: int):

        if valueToInsert in self.uniqueValueHolder:
            return

        lowIdx = 0
        highIdx = len(self.orderedArr)-1

        while lowIdx <= highIdx:
            midIdx = (highIdx+lowIdx)//2


            if self.orderedArr[midIdx] > valueToInsert:
                highIdx = midIdx-1

            elif self.orderedArr[midIdx] < valueToInsert:
                lowIdx = midIdx+1

        self.orderedArr = self.orderedArr[0:lowIdx] + [valueToInsert] + self.orderedArr[lowIdx:len(self.orderedArr)]
        print(self.orderedArr)


binaryInsert = binaryInsert()

binaryInsert.insert(2)
binaryInsert.insert(7)
binaryInsert.insert(-1)
binaryInsert.insert(5)
binaryInsert.insert(100)
binaryInsert.insert(8)
binaryInsert.insert(-3)
binaryInsert.insert(-2)
