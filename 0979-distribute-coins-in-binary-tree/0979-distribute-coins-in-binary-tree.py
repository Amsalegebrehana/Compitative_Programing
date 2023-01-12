# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        move = 0
        def dfs(node):
            nonlocal move
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            move += abs(left)
            move += abs(right)
            return node.val + left + right -1
        dfs(root)
        return move