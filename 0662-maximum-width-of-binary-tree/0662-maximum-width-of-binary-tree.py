# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        levels =  defaultdict(list)
        maxwidth = 0
        
        def dfs(node,level, l):
            if not node:
                return 0
            levels[level] += [l]
            dfs(node.left, level+1, 2 * l - 1)
 
            dfs(node.right, level+1, 2 * l)
       
        dfs(root,0, 1)

        for l in levels:
            maxwidth = max(maxwidth, levels[l][-1] - levels[l][0] + 1)
        return maxwidth