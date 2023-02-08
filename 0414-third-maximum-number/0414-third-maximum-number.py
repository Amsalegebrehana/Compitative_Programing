class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxnum = max(nums)
        nums = list(set(nums))

        nums.sort()
        if len(nums) < 3:
            return maxnum
        for i in range(len(nums), -1, -1):
            if i == len(nums) - 3:
                return nums[i]
            