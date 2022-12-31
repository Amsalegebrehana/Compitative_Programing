class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        presum = [nums[0]]
        idx = 0
        n = len(nums)
        mindiff = inf

        for i in range(1,len(nums)):
            presum.append(presum[-1] + nums[i])

        for i in range(len(presum)):
            div = n - (i+1)
            if n - (i+1) == 0:
                div = n 
            
            diff = abs((presum[i]//(i+1)) - ((presum[-1]- presum[i])//(div)))
            if diff < mindiff:
                mindiff = diff
                idx = i
     
        return idx