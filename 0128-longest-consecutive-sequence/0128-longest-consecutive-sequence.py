class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     
        if len(nums) == 0:
            return 0
        nums.sort()
        max_len = 0
        length = 1
        for i in range(1,len(nums)):
            if nums[i - 1] != nums[i]:
                if nums[i - 1] + 1 == nums[i]:
                    length += 1
                else:
                    max_len = max(max_len, length)

                    length = 1
        max_len = max(max_len, length)
        return max_len
        