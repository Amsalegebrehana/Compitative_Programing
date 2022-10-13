# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if root.right:
                cur = root.right
                while cur.left != None:
                    cur = cur.left
                cur.left = root.left
                return root.right
            else:
                return root.left
        
        
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        
        return root