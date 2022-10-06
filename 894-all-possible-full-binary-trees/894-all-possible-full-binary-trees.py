# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {0:[], 1:[TreeNode(0)]}
        if n % 2 == 0: return []
       
        def rec(n):
            if n % 2 == 0: return []
            if n not in memo:
                ans = []
                for x in range(n):
                    y = n -1 - x
                    for l in rec(x):
                        for r in rec(y):
                            node = TreeNode(0)
                            node.left = l
                            node.right = r
                            ans.append(node)
                memo[n] = ans
          
            return memo[n]
        return rec(n)
                