class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
    
        max_len = 1
        left = 0
        curr = nums[left]
        for i in range(1,len(nums)):
            while curr & nums[i] != 0:
              
                curr -= nums[left]
                left +=1
            max_len = max(max_len, i - left + 1)
            curr += nums[i]
        return max_len
        
        