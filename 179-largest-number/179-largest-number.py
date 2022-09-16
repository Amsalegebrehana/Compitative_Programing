class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
               
                j+=1
            i+=1
        l = [str(i) for i in nums]
     
        return str(int("".join(l)))