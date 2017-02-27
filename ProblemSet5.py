from collections import Counter,defaultdict
from HeapTest import MinHeap, Node
from TreePrint import printTree, printCodes
from helper import makeHuffmanInput
from math import log
from random import choices, randrange
import string

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


total_operations = 0

def string2freq(read_string): # x is a string of symbols from alphabet.
    S = sorted(set(read_string)) #Sorts and takes only unique elemetns from read_string
    #O(n log(n))
    f = list() #creates a list
    for character in S: #for all char in S
        f.append(read_string.count(character)) #adds the number of times something appears in read_string to f
    return S, f

def huffmanEncode(S, f): # f is a vector of symbol frequencies, from above
    """
    Create a minHeap and add the nodes into it.
    """
    insert_count = 0
    build_count = 0

    H = MinHeap() # H.initialize
    n = len(f)
    for i in range(n): #O(n) to insert each n.
        new_nochild_node = Node(f[i], S[i], None, None) #No children because they are the lowest. Constant time
        H.insert(new_nochild_node) #Insert frequency, characater
        insert_count+=1

    root_node = None
    while(True): #O(n log(n)) time for insertion and then extraction
        """
        Returns the lowest nodes on the tree to build the Huffman tree.
        """
        if (len(H.hList) > 2): #Runs when at least two items remain in the heap
            i = H.delMin() #Collect two minimum frequency nodes from heap
            j = H.delMin()
            k_sum = i.freq + j.freq #sum those frequencies to make huffman tree
            new_node = Node(k_sum, -1, i, j)
            build_count+=1
            H.insert(new_node) #Add that single node back in to heap
        else:
            print(build_count)
            build_count = log(build_count,2) #Take the log base 2 of each count for this step.
            break #Stops while loop when 2 or less items remain in the heap
    root_node = H.hList[1] #associates the last item on the heap as the root node

    ####################################

    adict = dict(printCodes(root_node,"")) #Passes in the root node into a recursive function
    #this recursive function will return a list of characters with their corresponding binary code.

    return adict, insert_count * build_count


def encodeString(x, T): #verbatim from the writeup. Compiles all the code's togeather.
    y = ""
    for ii in range(1, len(x)):
        y = y + T[x[ii]]
    return y



# S, f = string2freq(read_in_string)
# adict = huffmanEncode(S, f)
# y = encodeString(read_in_string, adict)

# print(y)
# print(len(y))

input_size = 2000
randChar = sorted(set(''.join(choices(string.ascii_lowercase, k=input_size))))
adict, operation = huffmanEncode(randChar,makeHuffmanInput(len(randChar)))

print(adict)
print(operation)
