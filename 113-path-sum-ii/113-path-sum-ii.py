# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def rec(root, val, path):
            if not root:
                return 0
            if not root.left and not root.right and val == targetSum:
                res.append(path)
            else:
                if root.left:
                    rec(root.left, root.left.val + val, path+[root.left.val])
                if root.right:
                    rec(root.right, root.right.val + val, path+[root.right.val])
        if not root:
            return res
        rec(root, root.val, [root.val])
        
        return res
            
            