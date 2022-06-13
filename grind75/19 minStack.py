import sys


class MinStack:

    def __init__(self):
        self.stackArr = []
 
    def push(self, val: int) -> None:
        currMin = self.getMin()
        if val < currMin:
            currMin=val
        self.stackArr.append( (val, currMin))

    def pop(self) -> None:
        self.stackArr.pop()

    def top(self) -> int:
        return self.stackArr[-1][0]

    def getMin(self) -> int:
        return self.stackArr[-1][1] if len(self.stackArr) > 0 else sys.maxsize
