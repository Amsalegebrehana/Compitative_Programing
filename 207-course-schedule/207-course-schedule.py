class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ans = 0
        indegree = [0] * numCourses
 
        outgoing = defaultdict(set)
        for i, j in prerequisites:
            outgoing[j].add(i)
            indegree[i] += 1
     
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            size = len(queue)
            ans+=1
            for i in outgoing[curr]:
                indegree[i]-=1
                if indegree[i] == 0:
                     queue.append(i)
                    
       
        return ans == numCourses