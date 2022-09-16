from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        res, left, right = 1, 0, 0
        sortedl = SortedList()
        while left<=right and  right < len(nums):
            sortedl.add(nums[right])
            if abs(sortedl[-1] - sortedl[0]) <= limit:
                res = max(res, right - left + 1)
                right +=1
            else:
                sortedl.remove(nums[left])
                left +=1
                right +=1
            
    
        return res