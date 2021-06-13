
class Solution:

    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slowNode = head.next
        fastNode = head.next.next

        while fastNode is not None and slowNode is not None and slowNode != fastNode:
            slowNode = slowNode.next
            if fastNode.next is None:
                return None
            fastNode = fastNode.next.next
        
        if fastNode is None or slowNode is None:
            return None

        slowNode = head
        while slowNode != fastNode:
            slowNode = slowNode.next
            fastNode = fastNode.next

        return slowNode