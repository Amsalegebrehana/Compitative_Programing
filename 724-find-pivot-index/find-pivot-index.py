class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref_sum = [nums[0]]
        for i in range(1,len(nums)):
            pref_sum.append(pref_sum[-1] + nums[i])

        for i in range(len(nums)):
            if pref_sum[i] - nums[i]  == (pref_sum[len(pref_sum) - 1] - pref_sum[i]):
            
                return i

        return -1
            
        