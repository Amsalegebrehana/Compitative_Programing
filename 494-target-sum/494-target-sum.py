class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def rec(i, total):
            if i == len(nums):
                return 1 if total== target else 0
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = (rec(i + 1, total + nums[i]) + rec(i + 1, total - nums[i]))
            return dp[(i,total)] 
        return rec(0,0)