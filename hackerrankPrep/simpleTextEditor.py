import sys
def textEditor(input, sStack, prevStr):

    ##split input to get operation and following text if there is any

    inputList = input.split()

    if inputList[0] == '1':
        ##append inputList[1]
        sStack.append(prevStr)
        newStr = prevStr + inputList[1]
        return newStr, sStack

    if inputList[0] == '2':
        ##delete k chars of S
        sStack.append(prevStr)
        return prevStr[:len(prevStr)-int(inputList[1])], sStack

    if inputList[0] == '3':
        ##print kth char of S

        print(prevStr[int(inputList[1]) -1])
        return prevStr, sStack

    if inputList[0] == '4':
        ##undo
        
        newStr = sStack.pop()
        return newStr, sStack


passedQ = False
stack=[]
prev=""

for line in sys.stdin:
    


    if passedQ:
        prev, stack = textEditor(line, stack, prev)

        
    passedQ=True
