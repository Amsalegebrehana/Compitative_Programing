# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = 0
        def rec(root):
            nonlocal c
            
            if not root:
                return 
            left = rec(root.left)
            if left:
                return left
        
            c += 1
            if c == k:
               
                return root.val
           
            return rec(root.right)
        ans = rec(root) 
        return ans if ans else 0