# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node, i):
            if not node:
                return 
            if i >= len(result):
                result.append(node.val)
            dfs(node.right, i+1)
            dfs(node.left, i+1)
        dfs(root, 0)
        return result