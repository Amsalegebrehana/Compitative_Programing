class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        maxic = 0
        ts = 0
        for i in range(len(costs)):
            ts += costs[i]

            if ts <= coins:
                maxic +=1
            else:
                break
        return maxic