from collections import Counter,defaultdict

def string2freq(x): # x is a string of symbols from alphabet.
    S = sorted(set(x))
    f = list()

    for character in S:
        f.append(x.count(character))

    return S, f

def huffmanEncode(S, f): # f is a vector of symbol frequencies, from above
    #TODO: Heap = minheap() // initialize minHeap
    print('s')

def encodeString():
    # TODO:
    print('s')

print(string2freq("aaasssssssssdd"))
