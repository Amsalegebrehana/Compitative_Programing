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
            curr = 0
            if root.left and root.left.val == root.val:
                curr += l
            else:
                l = 0
            if root.right and root.right.val == root.val:
                curr += r
            else:
                r = 0
            maxpath = max(maxpath, curr)
            return max(l, r) + 1
        dfs(root)
        return maxpath
                