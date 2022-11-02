class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        memo = {}
        def dp(i, flag, prev):
            if i >= len(nums):
                return 0
            nojump = 0
            jump = 0
            if (i, flag, prev) not in memo:
                if flag:
                    if nums[i] > prev:
                        nojump = 1 + dp(i + 1, False, nums[i])
                 
                    jump = dp(i + 1, flag, prev)
                else:
                    if nums[i] < prev:
                        nojump = 1 + dp(i + 1, True, nums[i])
                 
                    jump = dp(i + 1, flag , prev)
                memo[(i, flag, prev)] =  max(nojump, jump) 
            return memo[(i, flag, prev)]
        return max(dp(0, True, -1), dp(0,False,1001)) 
       