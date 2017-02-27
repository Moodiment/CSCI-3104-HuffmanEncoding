from random import randrange
def makeHuffmanInput(n):
    f = []
    for ii in range(1,n):
        f.append(randrange(1,100))
    return f
