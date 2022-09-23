# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(set)
        queue= deque([root])
        while queue:
            
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    graph[curr.val].add(curr.left.val)
                    graph[curr.left.val].add(curr.val)
                if curr.right:
                    queue.append(curr.right)
                    graph[curr.val].add(curr.right.val)
                    graph[curr.right.val].add(curr.val)
                    
        queue2 = deque([start])
        visited = {start}
        nummin = -1
        while queue2:
            size = len(queue2)
         
           
            for i in range(size):
                
                curr = queue2.popleft()
                for i in graph[curr]:
                    if i not in visited:
                        queue2.append(i)
                        visited.add(i)

            nummin +=1
    
        return nummin           
        