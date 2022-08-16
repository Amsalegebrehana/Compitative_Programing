# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None or left.val != right.val:
                return False
            return rec(left.left, right.right) and rec(left.right, right.left)
        return rec(root.left, root.right)