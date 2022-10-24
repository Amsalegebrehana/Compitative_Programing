class Solution:
    def rob(self, nums: List[int]) -> int:
        memo ={}
        def dp(i):
            if i == len(nums) or i == len(nums) + 1:
                return 0
       
            if i not in memo:
                nojump = nums[i] + dp(i + 2)
                jump = dp(i + 1)
                memo[i] = max(jump, nojump)
            return memo[i]
        return max(dp(0),dp(1))