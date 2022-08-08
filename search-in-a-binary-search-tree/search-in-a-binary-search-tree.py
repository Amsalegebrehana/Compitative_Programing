# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def rec(root):
            if not root:
                return
            if root.val == val:
                return root
            if root.val > val:
                return rec(root.left)
            else:
                return rec(root.right)
        return rec(root)
                
            
        