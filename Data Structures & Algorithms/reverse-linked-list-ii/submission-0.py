class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        currentNode = head
        prev = dummy
        count = 1

        while count!=left:
            prev = currentNode
            currentNode = currentNode.next
            count+=1

        prevReversed = None
        connection = prev
        tail = currentNode
        i = 0
        while i<(right-left+1):
            nextTemp = currentNode.next
            currentNode.next = prevReversed
            prevReversed = currentNode
            currentNode = nextTemp
            i+=1
        connection.next = prevReversed
        tail.next = currentNode
        
        return dummy.next