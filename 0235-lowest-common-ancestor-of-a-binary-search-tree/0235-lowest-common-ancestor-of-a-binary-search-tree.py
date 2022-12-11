# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return 
            if p.val < root.val and q.val < root.val:
                return dfs(root.left)
            elif p.val > root.val and q.val > root.val:
                return dfs(root.right)
            elif p.val == root.val or q.val == root.val:
                return root
            else:
                return root
        return dfs(root)
                
        
            
        