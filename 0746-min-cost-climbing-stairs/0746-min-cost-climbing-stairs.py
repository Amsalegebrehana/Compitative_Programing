class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(i):
            if i == len(cost) or i == len(cost)+1:
                return 0
            if i not in memo:
                twojump = cost[i] + dp(i + 2)
                onejump = cost[i] + dp(i + 1)
                memo[i] = min(twojump, onejump)
            return memo[i]
        return min(dp(0), dp(1))