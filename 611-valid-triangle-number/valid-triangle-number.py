class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result = 0

        for i in range(len(nums) - 1, -1, -1):
            j = i - 1
            k = 0
            while k < j:
                if nums[k] + nums[j] > nums[i]:
                    result = result + j - k
                    j -=1
                else:
                    k +=1

        return result
                        
        