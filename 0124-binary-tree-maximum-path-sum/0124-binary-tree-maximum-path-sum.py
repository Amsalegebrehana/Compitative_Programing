# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float('-inf')
        def dfs(root):
            nonlocal maxsum
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            left , right = 0 , 0
            if root.left:
                left = max(left,l)
            if root.right:
                right = max(right,r)
           
            maxsum = max(maxsum, left + right + root.val)
            return max(left, right) + root.val
        dfs(root)

        return maxsum