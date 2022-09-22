# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.lsum = 0
        def inorder(root):
            if root.left:
                if not root.left.left and not root.left.right:
                    self.lsum += root.left.val
                inorder(root.left)
            if root.right:
               
                inorder(root.right)
        inorder(root)
  
        return self.lsum