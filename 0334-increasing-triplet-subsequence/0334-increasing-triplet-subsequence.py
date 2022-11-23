class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minval = nums[0]
        maxval = inf
        for num in nums:
            if num< minval:
                minval = num
            elif num > maxval:
                return True
            elif minval < num < maxval:
                maxval = num
        return False
                
            