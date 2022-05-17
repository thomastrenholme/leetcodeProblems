import sys


class queue:
    
    ##1 is enqueue
    ##2 is dequeue
    #3 is print element at front of queue 
    def __init__(self):
        self.queueArr = []

    def enqueue(self, x):
        self.queueArr.append(x)
        
    def dequeue(self):
        self.queueArr.pop(0)

    def printFunc(self):
        if self.queueArr:
            print(self.queueArr[0])

myQueue = queue()
for line in sys.stdin:
    
    lineArr = line.split()
    

    if int(lineArr[0]) == 1:
        myQueue.enqueue(int(lineArr[1]))

    elif int(lineArr[0]) == 2:
        myQueue.dequeue()

    else:
        myQueue.printFunc()