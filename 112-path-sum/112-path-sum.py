# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def rec(root, summ):
            if not root:
                return 0
            if not root.left and not root.right:
               
                return summ == targetSum
            else:
                left = right = False
                if root.left:
                    left = rec(root.left, summ + root.left.val)
                    
                if root.right:
                    right = rec(root.right, summ + root.right.val)
                return left or right
        if not root:
            return False
        return rec(root, root.val) 
            
            
        