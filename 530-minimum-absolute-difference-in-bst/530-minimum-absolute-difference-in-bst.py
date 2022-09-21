# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            l.append(root.val)
            dfs(root.right)
        dfs(root)
        mv = 100000
        for i in range(len(l)-1,0,-1):
            mv = min(mv, l[i]-l[i-1])
        return mv