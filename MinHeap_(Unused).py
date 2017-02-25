class MinHeap:
  def __init__(self):
    self.heapList = []
    self.currentsSize = 0

    def bubbUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i//2]
    def DFTInOrder(H ,i):#H is the heep I is the index for the tree
        # want to find the child that corresponds to i
        #go up to the parent from i
        s="" #empty string for the encoder which we will return
        while i != 1:
            j =i/2 # parent of the node
            #test if it is right or left node
            if j == i*2+1 : s+"i"
            else: s+"0"
            i-=1
        return s
