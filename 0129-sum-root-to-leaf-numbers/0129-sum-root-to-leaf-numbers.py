# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def dfs(curr_root, path):
            nonlocal summ
            if not curr_root:
                return 
            if curr_root and not curr_root.left and not curr_root.right:
                summ += int(path)
            if curr_root.left: 
                dfs(curr_root.left, path + str(curr_root.left.val))
         
            if curr_root.right:
                dfs(curr_root.right, path + str(curr_root.right.val))
      
        dfs(root, str(root.val))
       
        return summ 