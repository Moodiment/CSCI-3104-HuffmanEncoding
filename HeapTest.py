

class Node:
    def __init__(self, freq,char,leftNode,rightNode):
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
        self.hList = [0] #We must start with one element in the heap for integer division
        # Current size of heap.
        self.currentSize = 0

        while i // 2 > 0: #While loop to recursively move up the tree.
            if self.hList[i].freq < self.hList[i // 2].freq: #Check to see if parent is greater than child
                temp = self.hList[i // 2] #Save parent in temporary
                self.hList[i // 2] = self.hList[i] #Assign child as parent
                self.hList[i] = temp #Assign parent as child.
            i = i // 2 #Move to next height.

      self.hList.append(Node1) #Add the tuple, frequency and character to the end of the Heap
      self.currentSize = self.currentSize + 1 #Incriment the Heap

      if i * 2 + 1 > self.currentSize:
      else:
          if self.hList[i*2].freq < self.hList[i*2+1].freq:
          else:

      retval = self.hList[1] #Pops the top value off the que
      self.hList[1] = self.hList[self.currentSize] #Collects the last item in the que and replaces it with the popped item
      self.currentSize = self.currentSize - 1 #Decrements current size cause we're deleting
      self.hList.pop() # Pops lowest value off list


bh = MinHeap()

bh.insert
