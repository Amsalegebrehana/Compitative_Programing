class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
       
        def minn(nums):
            min_num = max(nums)
            for i in nums:
                if i < min_num and i !=0:
                    min_num = i
            return min_num
       
        min_num = minn(nums)
        count = 0
        while min_num !=0:
           
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = nums[i] - min_num
            count +=1
          
            min_num = minn(nums)
        return count