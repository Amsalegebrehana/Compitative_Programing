class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dictt = defaultdict(set)
        
        for i, j in logs:
            dictt[i].add(j)
      
        result = [0] * k
        for i in dictt.values():
            n = len(i)
           
            result[n-1] += 1
        return result