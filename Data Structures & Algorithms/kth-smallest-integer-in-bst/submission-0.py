# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def traverse(root, k, arr):
            if root is None:
                return
            traverse(root.left, k, arr)
            arr.append(root.val)
            traverse(root.right, k, arr)
            return arr
        arr = traverse(root, k, arr)
        return arr[k-1]
        