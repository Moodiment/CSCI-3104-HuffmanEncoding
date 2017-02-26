from collections import Counter,defaultdict
from HeapTest import MinHeap, Node
import DFTInorder

read_in_string="the road not taken by robert frost two roads diverged in a yellow wood, and \
sorry i could not travel both and be one traveler, long i stood and looked down\
 one as far as i could to where it bent in the undergrowth; then took the other,\
  as just as fair, and having perhaps the better claim, because it was grassy \
  and wanted wear; though as for that the passing there had worn them really \
  about the same, and both that morning equally lay in leaves no step had trodden\
   black. oh, i kept the first for another day! yet knowing how way leads on to \
   way, i doubted if i should ever come back. i shall be telling this with a sigh\
    somewhere ages and ages hence: two roads diverged in a wood, and i- i took \
    the one less traveled by, and that has made all the difference."

def string2freq(read_string): # x is a string of symbols from alphabet.
    S = sorted(set(read_string)) #Can I use this?
    f = list()
    for character in S:
        f.append(read_string.count(character))
    return S, f

def huffmanEncode(S, f): # f is a vector of symbol frequencies, from above
#create huffman tree. Depth first search on huffman encode, add binary code to dictionary with key as key.
    #TODO: Heap = minheap() // initialize minHeap from class.
    H = MinHeap() # H.initialize
    n = len(f)
    for i in range(n):
        new_node = Node(f[i], S[i], None, None)
        H.insert(new_node) #Insert frequency, characater
        # print(new_node.freq)
        # print(new_node.char)
        # input()
    for i in range(H.currentSize):
        item = H.hList[i+1]
        print(item)
        if(item.leftNode or item.rightNode):
            print(item.leftNode.char)
        else: print("NONE")
        input()
        #Now I need to assocaite old node (base of huffman) with new node

    # k = n+1
    # n = 2*n-1
    # for k in range(n+1, 2*n-1):
    #     i = H.delMin() #Return a tuple from the lowest element
    #     j = H.delMin()
    #
    #     # f[k] = f[i] + f[j]
    #     TempNode = Node(i[0]+j[0],-1,i,j)
    #     print(TempNode)
    #
    #     input()
    #
    # T = []
    # for i in n:
    #     T.append(DFTInOrder(H, i))
    #
    # return T

def encodeString():
    return


S, f = string2freq(read_in_string)
#print(str(S)+" " + str(f))
huffmanEncode(S, f)



#Testing...

#print(string2freq("asd!!!$$###fasdas"))
