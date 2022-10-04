class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manemployee = collections.defaultdict(list)
        for i in range(n):
            manemployee[manager[i]].append(i)
        queue = deque([(headID, informTime[headID])])
   
        ans = 0
        while queue:
            curr,curr_time = queue.popleft()
            ans = max(ans, curr_time)
            for i in manemployee[curr]:
           
                queue.append((i, curr_time + informTime[i]))
           
        return ans