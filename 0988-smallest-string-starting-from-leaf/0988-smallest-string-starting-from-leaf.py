# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = "z" * 8500
        def dfs(curr_root,word):
            nonlocal result
            if not curr_root:
                return ''
            if curr_root and not curr_root.left and not curr_root.right:
                
                if word < result:
                    result = word
            if curr_root.left:
                dfs(curr_root.left, chr(curr_root.left.val + ord('a')) + word)
            if curr_root.right:
                dfs(curr_root.right, chr(curr_root.right.val  + ord('a') )+ word)
        dfs(root, chr(root.val + ord('a')))
        return result
                
            
        