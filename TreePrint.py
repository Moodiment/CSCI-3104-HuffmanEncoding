from collections import Counter
def printTree(node): #Not sure if this works.
    print("Current tree:")
    print(node.freq)
    print(node.char)
    print("End\n")
    # print(node.leftNode)
    # print(node.rightNode)
    if(node.leftNode):
        printTree(node.leftNode)
    if(node.rightNode):
        printTree(node.rightNode)
    # else: print("END")

def printCodes(node,code): #Runtime of O(n)

    if (not node):
        return
    if (node.char != -1):
        print(node.char+ " : " + code)


    printCodes(node.leftNode, code+"0")
    printCodes(node.rightNode, code+"1")
