# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(node, res):
            if node is None:
                return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
            return res
        res = inorder(root, res)
        return res[k-1]

        