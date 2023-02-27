class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ct=[0]*101
        
        for b,d in logs:
            ct[b-1950]+=1
            ct[d-1950]-=1
            
        idx=0
        mx=0
        ps=0
        
        for i,c in enumerate(ct):
            ps+=c
            if ps>mx:
                mx=ps
                idx=i
        return idx+1950