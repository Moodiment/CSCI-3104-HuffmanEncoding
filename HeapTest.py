

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

    def BubbleUp(self,i, operations_counter):
        while i // 2 > 0: #While loop to recursively move up the tree.
            if self.hList[i].freq < self.hList[i // 2].freq: #Check to see if parent is greater than child
                temp = self.hList[i // 2] #Save parent in temporary
                self.hList[i // 2] = self.hList[i] #Assign child as parent
                self.hList[i] = temp #Assign parent as child.
                operations_counter = operations_counter + 1
            i = i // 2 #Move to next height.
        return operations_counter

    def BubbleDown(self,i, operations_counter):
        while (i * 2) <= self.currentSize: #While loop to move down the tree.
            mc, operations_counter = self.FindChild(i, operations_counter) # Search for minimum child given i.
            if self.hList[i].freq > self.hList[mc].freq: #Compares the minimum child from the current node
                tmp = self.hList[i] #same as bubbleup, but for bubble down.
                self.hList[i] = self.hList[mc]
                self.hList[mc] = tmp
                operations_counter = operations_counter + 1
            i = mc
        return operations_counter

    def insert(self, Node1, operations_counter):
      self.hList.append(Node1) #Add the tuple, frequency and character to the end of the Heap
      self.currentSize = self.currentSize + 1 #Incriment the Heap
      operations_counter = self.BubbleUp(self.currentSize, operations_counter) # Because we added the tuple to the end of the list, we need to bubble it up
      return operations_counter

    def FindChild(self,i, operations_counter):
      if i * 2 + 1 > self.currentSize:
          return i * 2, operations_counter
      else:
          if self.hList[i*2].freq < self.hList[i*2+1].freq:
              return i * 2, operations_counter
          else:
              return i * 2 + 1, operations_counter

    def delMin(self, operations_counter):
      retval = self.hList[1] #Pops the top value off the que
      self.hList[1] = self.hList[self.currentSize] #Collects the last item in the que and replaces it with the popped item
      self.currentSize = self.currentSize - 1 #Decrements current size cause we're deleting
      self.hList.pop() # Pops lowest value off list
      operations_counter = self.BubbleDown(1, operations_counter) #Bubbles d own the first element in the list
      return retval, operations_counter

      def operationCount(self): #UNUSED/Depriciated.
          pass


bh = MinHeap()

bh.insert
