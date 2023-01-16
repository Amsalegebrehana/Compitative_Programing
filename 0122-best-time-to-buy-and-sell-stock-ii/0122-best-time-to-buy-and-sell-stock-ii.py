class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        max_profit = 0
        memo = {}
        
        def dp(i, flag):
            if i >= len(prices):
                return 0
            
            profit = 0
            
            if (i,flag) not in memo:
                jump = dp(i+1, flag)
                if flag:
                    profit = prices[i] + dp(i+1, False)
                else:
                    profit = -prices[i] + dp(i+1, True)

                memo[(i,flag)] = max(profit, jump)
            
            return memo[(i,flag)]
        
        return max(dp(0,False), dp(1,False))