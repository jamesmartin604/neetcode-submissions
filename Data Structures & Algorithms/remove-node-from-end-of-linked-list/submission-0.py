# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        currentNode = head
        while currentNode:
            temp = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = temp

        currentNode = prev
        prevNode = None
        count = 1
        while currentNode and count<n:
            prevNode = currentNode
            currentNode = currentNode.next
            count+=1
        if prevNode:
            prevNode.next = currentNode.next
        else:
            prev = currentNode.next
        head = None
        currentNode = prev
        while currentNode:
            temp = currentNode.next
            currentNode.next = head
            head = currentNode
            currentNode = temp
        return head
        