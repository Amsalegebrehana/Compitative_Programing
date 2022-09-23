# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
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
                    
        queue2 = deque([target.val])
        visited = {target.val}
        ans = []
        while queue2:
            size = len(queue2)
         
            if k == 0:
                ans =  queue2
                break
            for i in range(size):
                
                curr = queue2.popleft()
                for i in graph[curr]:
                    if i not in visited:
                        queue2.append(i)
                        visited.add(i)
            k-=1

        return list(ans)
        