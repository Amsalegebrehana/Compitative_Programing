class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def dp(i,  j):
            ch1 = 0
            ch2 = 0
            if i >len(nums)-1 or j <0 or i > j:
                return 0
           
            else:
                if (i,  j) not in memo:
                    ch1 = nums[i] + min(dp(i+1, j-1), dp(i+2, j))

                    ch2 = nums[j] +  min(dp(i+1,  j-1), dp(i,  j-2))
                    memo[(i,  j)]= max(ch1, ch2)
            return memo[(i,  j)]
        p1 = dp(0, len(nums) - 1)
 
        return p1>= sum(nums)-p1