class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalSum =( len(nums) * (len(nums) + 1)) // 2
        summ = 0
        for i in nums:
            summ += i
        return totalSum - summ