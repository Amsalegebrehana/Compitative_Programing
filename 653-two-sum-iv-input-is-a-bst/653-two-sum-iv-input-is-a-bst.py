# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sett = set()
        def dfs(root):
            if not root:
                return False
            l = dfs(root.left)
          
            if k - root.val in sett:
                return True
            sett.add(root.val)
            r = dfs(root.right)
            return l or r
        return dfs(root)