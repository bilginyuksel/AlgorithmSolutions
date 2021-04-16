class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class QueueNode:
    def __init__(self, listIdx, listNode):
        self.listNode = listNode
        self.listIdx = listIdx
        self.val = self.listNode.val

class MinHeap:
    
    def __init__(self):
        self.heap = []

    def getParentIdx(self, idx):
        return (idx -1) // 2

    def getLeftIdx(self, idx):
        return (idx * 2) + 1

    def getRightIdx(self, idx):
        return (idx * 2) + 2

    def swap(self, firstIndex, secondIndex):
        self.heap[firstIndex], self.heap[secondIndex] = self.heap[secondIdx], self.heap[firstIndex]

    def isEmpty(self):
        return len(self.heap) == 0

    def siftUp(self, childIdx):
        parentIdx = self.getParentIdx(childIdx)
        while parentIdx >= 0 and self.heap[parentIdx].val > self.heap[childIdx].val:
            self.swap(parentIdx, childIdx)
            childIdx = parentIdx
            parentIdx = self.getParentIdx(childIdx)

    def siftDown(self, parentIdx):
        minIdx = parentIdx
        leftIdx = self.getLeftIdx(parentIdx)
        rightIdx = self.getRightIdx(parentIdx)

        if leftIdx < len(self.heap) and self.heap[leftIdx].val < self.heap[minIdx].val:
            minIdx = leftIdx

        if rightIdx < len(self.heap) and self.heap[rightIdx].val < self.heap[minIdx].val:
            minIdx = rightIdx

        if minIdx != parentIdx:
            self.swap(minIdx, parentIdx)
            self.siftDown(minIdx)

    def insert(self, listIdx, listNode):
        self.heap.append(QueueNode(listIdx, listNode))
        self.siftUp(len(self.heap)-1)

    def remove(self):
        self.swap(0, -1)
        removedElement = self.heap.pop()
        self.siftDown(0)
        return removedElement


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        queue = MinHeap()
        head = None
        mergedList = head

        for i in range(len(lists)):
            if lists[i] == None: continue
            queue.insert(i, lists[i])
            lists[i] = lists[i].next

        while not queue.isEmpty():
            queueNode = queue.remove()
            nextListIdx, currentListNode = queueNode.listIdx, queueNode.listNode
            if mergedList is not None:
                mergedList.next = currentListNode
                mergedList = mergedList.next
            else:
                head = currentListNode 
                mergedList = head

            if lists[nextListIdx] is not None:
                queue.insert(nextListIdx, lists[nextListIdx])
                lists[nextListIdx] = lists[nextListIdx].next

        return head

