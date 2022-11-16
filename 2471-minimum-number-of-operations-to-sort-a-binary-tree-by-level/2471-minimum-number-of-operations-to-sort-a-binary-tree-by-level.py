# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        swaps = 0
        def sortnum(nums):
            nonlocal swaps
            dictt = {}
            sortednums= sorted(nums)
            for i in range(len(nums)):
                dictt[nums[i]] = i
          
            for i in range(len(nums)):
                if nums[i] != sortednums[i]:
                   
                    prev = nums[i]
                    nums[i], nums[dictt[sortednums[i]]] = nums[dictt[sortednums[i]]], nums[i]
                    dictt[prev] = dictt[sortednums[i]]
                  
                    dictt[sortednums[i]] = i
                    swaps +=1
          
            return swaps
        level = 0
        queue = deque([root])
        
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    temp.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    temp.append(curr.right.val)
         
            sortnum(temp)
         
        return swaps
                    
                