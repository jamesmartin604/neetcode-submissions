# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(root) -> int:
            if root is None:
                return 0
            return 1 + max(maxDepth(root.left),maxDepth(root.right))

        if root is None:
            return True
        leftHeight = maxDepth(root.left)
        rightHeight = maxDepth(root.right)
        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)
        return leftBalanced and rightBalanced and abs(leftHeight-rightHeight)<=1
        