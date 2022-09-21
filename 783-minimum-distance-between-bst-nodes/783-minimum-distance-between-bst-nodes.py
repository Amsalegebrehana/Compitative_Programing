# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = -1
        self.ans = 100000
        def inorder(root):
            if not root:
                return root
            inorder(root.left)
            if self.prev != -1: 
                self.ans = min( self.ans, abs(root.val - self.prev))
         
            self.prev = root.val
            inorder(root.right)
       
        inorder(root)

        return self.ans
                
        