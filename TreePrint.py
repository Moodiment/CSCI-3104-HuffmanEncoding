from collections import Counter
import ast
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

def printCodes(node,code):
    T = []
    if (node.char != -1):
        print(node.char)
        return [(node.char,code)]
        #return [(str(node.char)+ ":" + str(code))]


    T = T + printCodes(node.leftNode, code+"0")
    T = T + printCodes(node.rightNode, code+"1")

    return T
