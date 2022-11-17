class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = (10 ** 9) + 7
        result = [inf] * (n)
        result[0] = 0
  
        heap = [(0,0)]
        adj = defaultdict(set)
        for i, j, k in roads:
            adj[i].add((k,j))
            adj[j].add((k,i))

        ways= [0] * n
        ways[0] = 1
       
        while heap:
            time, node = heappop(heap)
           
            for nebour in adj[node]:
                
         
                if result[nebour[1]] > time + nebour[0]:
                    
                    result[nebour[1]] = time + nebour[0]
                    ways[nebour[1]] =  ways[node]
                    heappush(heap, (time + nebour[0], nebour[1]))
                   
                elif result[nebour[1]] == time + nebour[0]:
                    
                    ways[nebour[1]] =  (ways[nebour[1]] +  ways[node])  % mod


        return ways[n-1]
            


        