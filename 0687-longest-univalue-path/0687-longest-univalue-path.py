# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxpath = 0
        def dfs(root):
            nonlocal maxpath
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            left, right = 0, 0
            if root.left and root.left.val == root.val:
                left = l
           
            if root.right and root.right.val == root.val:
                right = r
          
            maxpath = max(maxpath, left + right)
            return max(left, right) + 1
        dfs(root)
        return maxpath
                