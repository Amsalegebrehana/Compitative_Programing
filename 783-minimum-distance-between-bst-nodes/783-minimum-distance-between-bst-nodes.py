# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        l = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            l.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)

        minval = l[-1]
        for i in range(len(l)-1,0,-1):
            minval = min(minval,l[i] - l[i-1])
   
        return minval
                
        