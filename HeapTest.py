from random import randrange

class Node:
    def __init__(self, freq,char,rightNode,leftNode):
        self.char = char
        self.freq = freq
        self.rightNode = rightNode
        self.leftNode = leftNode

        def setLeftNode(self, leftNode):
            self.leftNode = leftNode
        def setRightNode(self, rightNode):
            self.rightNode = rightNode

class MinHeap:
    def __init__(self): #Constructor
        # Initalize a list to used for tuple
        self.hList = [0]
        # Current size of heap.
        self.currentSize = 0

    def BubbleUp(self,i):
        while i // 2 > 0: #While loop to recursively move up the tree.
            if self.hList[i].freq < self.hList[i // 2].freq: #Check to see if parent is greater than child
                temp = self.hList[i // 2] #Save parent in temporary
                self.hList[i // 2] = self.hList[i] #Assign child as parent
                self.hList[i] = temp #Assign parent as child.
            i = i // 2 #Move to next height.

    def BubbleDown(self,i):
      while (i * 2) <= self.currentSize: #While loop to move down the tree.
          mc = self.FindChild(i) #
          if self.hList[i].freq > self.hList[mc].freq:
              tmp = self.hList[i]
              self.hList[i] = self.hList[mc]
              self.hList[mc] = tmp
          i = mc

    def insert(self, Node1):
      self.hList.append(Node1) #Add the tuple, frequency and character to the end of the Heap
      self.currentSize = self.currentSize + 1 #Incriment the Heap
      self.BubbleUp(self.currentSize) # Because we added the tuple to the end of the list, we need to bubble it up

    def FindChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.hList[i*2].freq < self.hList[i*2+1].freq:
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

bh.insert
