class MyQueue:

    def __init__(self):
        self.fifoArr = []
        self.secondArr = []
        self.topIdxCtr=0

    def push(self, x: int) -> None:
        self.fifoArr.append(x)

    def pop(self) -> int:
        if not self.empty():

            v = self.fifoArr[self.topIdxCtr]
            self.topIdxCtr+=1
            return v

    def peek(self) -> int:
        return self.fifoArr[self.topIdxCtr]
        
    def empty(self) -> bool:
        return self.topIdxCtr==len(self.fifoArr)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()