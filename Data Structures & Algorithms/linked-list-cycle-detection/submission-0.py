# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list = []
        currentNode = head
        while currentNode:
            if currentNode not in list:
                list.append(currentNode)
            else:
                return True
            currentNode = currentNode.next
        return False
        