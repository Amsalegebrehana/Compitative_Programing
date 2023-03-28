class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       
        nums.sort()
        left = 0
        right = len(nums) -1
        best = -inf
        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= mid:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
 
        return best