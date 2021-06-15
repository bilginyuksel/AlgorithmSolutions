
class BaseHeap:
    def __init__(self):
        self.heap = []
    
    def compare(self, array, firstIdx, secondIdx):
        raise NotImplementedError()

    def siftDown(self, parentIdx):
        if parentIdx >= len(self.heap):
            return

        leftChildIdx = self.getLeftIdx(parentIdx)
        rightChildIdx = self.getRightIdx(parentIdx)
        potentialSwapIdx = parentIdx

        if leftChildIdx < len(self.heap) and self.compare(self.heap, leftChildIdx, potentialSwapIdx):
            potentialSwapIdx = leftChildIdx
        
        if rightChildIdx < len(self.heap) and self.compare(self.heap, rightChildIdx, potentialSwapIdx):
            potentialSwapIdx = rightChildIdx

        if potentialSwapIdx != parentIdx:
            self.swap(self.heap, potentialSwapIdx, parentIdx)
            self.siftDown(potentialSwapIdx)

    def siftUp(self, idx):
        parentIdx = self.getParentIdx(idx)
        while parentIdx >= 0 and self.compare(self.heap, parentIdx, idx):
            self.swap(self.heap, idx, parentIdx)
            idx = parentIdx
            parentIdx = self.getParentIdx(idx)

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1)

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        elementToRemove = self.heap.pop()
        self.siftDown(0)
        return elementToRemove
    
    def removeValue(self, value):
        print(value)
        pass
    
    def peek(self):
        return self.heap[0]

    def isEmpty(self):
        return (self.heap) == 0

    def swap(self, arr, first, second):
        arr[first], arr[second] = arr[second], arr[first]

    def getLeftIdx(self, idx):
        return idx * 2 + 1

    def getRightIdx(self, idx):
        return idx * 2 + 2

    def getParentIdx(self, idx):
        return (idx -1) // 2


class MinHeap(BaseHeap):
    def compare(self, array, firstIdx, secondIdx):
        return array[firstIdx] > array[secondIdx]

class MaxHeap(BaseHeap):
    def compare(self, array, firstIdx, secondIdx):
        return array[firstIdx] < array[secondIdx]

class MedianUpdateSolution:

    def __init__(self) -> None:
        self.minHeap = MinHeap()
        self.maxHeap = MaxHeap()

    def append(self, value):
        self.minHeap.insert(value)

    def remove(self, value):
        self.minHeap.remove(value)

    def medianUpdate(self, operations):
        pass


arr = [10, 8, 5, 7, 12, 9, 2]
s = MedianUpdateSolution()
for elem in arr:
    s.append(elem)
    print(s.minHeap.heap)

