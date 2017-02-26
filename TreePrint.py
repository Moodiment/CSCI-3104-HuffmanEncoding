def printCodes(node): #Not sure if this works.
    print(node.freq)
    if(node.leftNode):
        printCodes(node.leftNode)
    elif(node.rightNode):
        printCodes(node.rightNode)
    else: print("END")
