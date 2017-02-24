class MinHeap:
  def __init__(self):
    self.heapList = []
    self.currentsSize = 0
    
    def bubbUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i//2]
