# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_path = math.inf
        def dfs(curr_root, path):
            nonlocal min_path
            if not curr_root:
                return 0
            if not curr_root.left and not curr_root.right:
                min_path = min(min_path, path)
            dfs(curr_root.left,path +1)
            dfs(curr_root.right, path+1)
        dfs(root, 1)
        return min_path if min_path != math.inf else 0
        