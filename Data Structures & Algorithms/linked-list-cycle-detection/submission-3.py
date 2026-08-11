# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        freq = []
        while head is not None:
            if head not in freq:
                freq.append(head)
            else:
                return True
            head = head.next
        return False
        