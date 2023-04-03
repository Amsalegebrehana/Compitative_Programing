class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        totalCost = 0
        diff = []
        
        for a,b in costs:
            diff.append(b - a)
            totalCost += a
        
        diff.sort()
      
        return totalCost + sum(diff[:len(diff)//2])
        