class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sumpplCityA = 0
        diffAB = []
        size = len(costs)

        for ca, cb in costs:
            sumpplCityA += ca
            diffAB.append(cb - ca)

        diffAB.sort()

        result = sumpplCityA +  sum(diffAB[:size // 2]) 

        return result