class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        left = 0
        while left < len(nums):
            if nums[left] <= 0:
                nums[left], nums[-1] = nums[-1], nums[left]
                nums.pop()
                left -=1
            left +=1
        if not nums:
            return 1
      
        for i in nums:
            if abs(i) < len(nums) + 1:
                nums[abs(i) - 1] = -1 * abs(nums[abs(i) - 1])
      
        for i in range(len(nums)):
            if nums[i]>0:
                return i + 1
        return len(nums) + 1
        