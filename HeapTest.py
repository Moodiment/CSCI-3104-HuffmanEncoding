#Heap test
class BinHeap:
    def __init__(self):
        # Initalize a list to used for tuple
        self.hList = [0]
        # Current size of heap.
        self.currentSize = 0

    def BubbleUp(self,i):
        while i // 2 > 0:
          if self.hList[i][0] < self.hList[i // 2][0]:
             tmp = self.hList[i // 2]
             self.hList[i // 2] = self.hList[i]
             self.hList[i] = tmp
          i = i // 2

    def insert(self,k, j):
      self.hList.append([k, j])
      self.currentSize = self.currentSize + 1
      self.BubbleUp(self.currentSize)


    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.hList[i][0] > self.hList[mc][0]:
              tmp = self.hList[i]
              self.hList[i] = self.hList[mc]
              self.hList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.hList[i*2][0] < self.hList[i*2+1][0]:
              return i * 2
          else:
              return i * 2 + 1

    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def delMin(self):
      retval = self.hList[1]
      self.hList[1] = self.hList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.hList.pop()
      self.percDown(1)
      return retval


bh = BinHeap()

#bh.buildHeap(["a","s","d"])


print(bh.insert(23,"a"))
print(bh.insert(2,"!"))
print(bh.insert(21,"sss"))
print(bh.insert(25,"asweqd"))

print(bh.delMin())
print(bh.delMin())

#print(bh.delMin())
