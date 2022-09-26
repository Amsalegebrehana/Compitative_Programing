# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        def dfs(root,path):
            if not root:
                return
            if not root.left and not root.right:
                self.ans.append(path)
            else:
                if root.left:
                    dfs(root.left, path + "->" + str(root.left.val))

                if root.right:
                    dfs(root.right, path + "->" + str(root.right.val))

        dfs(root, str(root.val))
        return self.ans
                
        