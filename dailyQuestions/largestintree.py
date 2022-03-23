from collections import deque



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(root):
        if not root:
            return
        queue= deque([root])
        maxx = 0
        ans = []
        
        while queue:
            maxx = queue[0].val
            for i in range(len(queue)):
                curr = queue.popleft()
               
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                maxx = max(maxx, curr.val)
                
            ans.append(maxx)
            
        return ans