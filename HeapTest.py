#Heap test
from random import randrange
class MinHeap:
    def __init__(self): #Constructor
        # Initalize a list to used for tuple
        self.hList = [0]
        # Current size of heap.
        self.currentSize = 0

    def BubbleUp(self,i):
        while i // 2 > 0: #While loop to recursively move up the tree.
          if self.hList[i][0] < self.hList[i // 2][0]: #Check to see if parent is greater than child
             temp = self.hList[i // 2] #Save parent in temporary
             self.hList[i // 2] = self.hList[i] #Assign child as parent
             self.hList[i] = temp #Assign parent as child.
          i = i // 2 #Move to next height.

    def BubbleDown(self,i):
      while (i * 2) <= self.currentSize: #While loop to move down the tree.
          mc = self.FindChild(i) #
          if self.hList[i][0] > self.hList[mc][0]:
              tmp = self.hList[i]
              self.hList[i] = self.hList[mc]
              self.hList[mc] = tmp
          i = mc

    def insert(self,k, j):
      self.hList.append([k, j]) #Add the tuple, frequency and character to the end of the Heap
      self.currentSize = self.currentSize + 1 #Incriment the Heap
      self.BubbleUp(self.currentSize) # Because we added the tuple to the end of the list, we need to bubble it up

    def FindChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.hList[i*2][0] < self.hList[i*2+1][0]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.hList[1]
      self.hList[1] = self.hList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.hList.pop()
      self.BubbleDown(1)
      return retval


bh = MinHeap()

#bh.buildHeap(["a","s","d"])


for x in range(randrange(20)):
    bh.insert(x,"s")



print(bh.delMin())
print(bh.delMin())

#print(bh.delMin())
