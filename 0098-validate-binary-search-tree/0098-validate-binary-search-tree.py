# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        def dfs(root):
            nonlocal prev
            if not root:
                return True
            l = r = True
            l = dfs(root.left)
            if prev != None and prev >= root.val:
                return False
            prev = root.val
            r = dfs(root.right)
            return l and r
            
      
        return dfs(root)
            