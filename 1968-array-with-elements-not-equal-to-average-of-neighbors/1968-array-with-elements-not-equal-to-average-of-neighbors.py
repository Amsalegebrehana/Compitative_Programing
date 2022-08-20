class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        i = 0
        left = 0
        right = len(nums)-1
        while i < len(nums):
            if i % 2 == 0:
                result.append(nums[left])
                left +=1
            else:
                result.append(nums[right])
                right-=1
            i+=1
        return result
        