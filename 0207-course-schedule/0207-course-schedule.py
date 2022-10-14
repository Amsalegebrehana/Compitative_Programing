class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incoming = [0] * numCourses
        outgoing = defaultdict(set)
        for i, j in prerequisites:
            
            incoming[i] += 1
            outgoing[j].add(i)
        queue = deque()
        for i in range(numCourses):
            if incoming[i] == 0:
                
                queue.append(i)
        
        visited = set()
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for i in outgoing[curr]:
                incoming[i] -=1
                if i not in visited and incoming[i] == 0:
                    queue.append(i)
                    visited.add(i)
        
        return len(ans) == numCourses
      
