class PriorityQueueNode:
    def __init__(self, priority) -> None:
        self.priority = priority

    def __repr__(self) -> str:
        return str(self.priority)

class PriorityQueue:

    def __init__(self, maxQueue=True) -> None:
        self.queue = []

        if maxQueue:
            self.comparator = self._maxComparator
        else:
            self.comparator = self._minComparator

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, value: PriorityQueueNode):
        self.queue.append(value)
        self._siftUp(len(self.queue)-1)

    def peek(self):
        if self.isEmpty():
            raise IndexError()

        return self.queue[0]

    def remove(self):
        if self.isEmpty():
            raise IndexError()

        self.swap(0, -1)
        removedElement = self.queue.pop()
        self._siftDown(0)
        return removedElement

    def _maxComparator(self, i, j):
        return i.priority < j.priority

    def _minComparator(self, i, j):
        return i.priority > j.priority

    def _getLeftIdx(self, parentIdx):
        return (parentIdx * 2) + 1

    def _getRightIdx(self, parentIdx):
        return (parentIdx * 2) + 2

    def _getParentIdx(self, childIdx):
        return (childIdx - 1) // 2

    def swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    def _siftUp(self, childIdx):
        parentIdx = self._getParentIdx(childIdx)

        while parentIdx >= 0 and self.comparator(self.queue[parentIdx], self.queue[childIdx]):
            self.swap(parentIdx, childIdx)
            childIdx = parentIdx
            parentIdx = self._getParentIdx(childIdx)

    def _siftDown(self, parentIdx):
        potentialIdx = parentIdx
        leftIdx = self._getLeftIdx(parentIdx)
        rightIdx = self._getRightIdx(parentIdx)

        if leftIdx < len(self.queue) and self.comparator(self.queue[potentialIdx], self.queue[leftIdx]):
            potentialIdx = leftIdx

        if rightIdx < len(self.queue) and self.comparator(self.queue[potentialIdx], self.queue[rightIdx]):
            potentialIdx = rightIdx

        if potentialIdx != parentIdx:
            self.swap(potentialIdx, parentIdx)
            self._siftDown(potentialIdx)

class MyNode(PriorityQueueNode):
    def __init__(self, priority, i, j) -> None:
        super().__init__(priority)
        self.i = i
        self.j = j
    
    def __repr__(self) -> str:
        return str(self.priority) + '-' + str(self.i) + '-' + str(self.j)

def tests():
    pq = PriorityQueue(maxQueue=False)

    pq.insert(MyNode(5, 1, 2))
    pq.insert(MyNode(12, 3, 2))
    pq.insert(MyNode(7, 4, 1))
    pq.insert(MyNode(18, 5, 2))

    print(pq.remove())
    print(pq.remove())
    print(pq.remove())
    print(pq.remove())

tests()