class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def rec(n):
            if n == 1: return 1
            if n == 2: return 2
            if n not in memo:
                memo[n] = rec(n-1) + rec(n-2)
            return memo[n]
        return rec(n)
                
        