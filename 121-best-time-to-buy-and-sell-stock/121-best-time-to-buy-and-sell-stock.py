class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if buy_day > prices[i]:
                buy_day = prices[i]
            max_profit = max(max_profit, prices[i] - buy_day)
        return max_profit