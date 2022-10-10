# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        presum = 0
        def dfs(root, presum):
            if not root:
                return presum
            presum = dfs(root.right,presum)
            root.val += presum
            presum = dfs(root.left,root.val)
            return presum
        dfs(root, presum)
        return root