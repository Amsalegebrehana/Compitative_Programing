# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lb, ub):
            if not root:
                return True
            if lb < root.val < ub:
                l = dfs(root.left, lb, root.val)
                
                r = dfs(root.right, root.val, ub)
                return l and r
            
            return False
        return dfs(root, float('-inf'), float('inf'))
            