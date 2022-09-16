class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(list)
        adjl =  defaultdict(list)
        for i,j in trust:
            adj[i].append(j)
            adjl[j].append(i)
    
        res = []
        for i in range(1,n+1):
            res.append((i,len(adj[i]), len(adjl[i])))
 
        for i in res:
            if i[1] == 0 and i[2] == n-1:
                return i[0]
            
        return -1
                
            