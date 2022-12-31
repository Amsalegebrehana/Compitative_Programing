class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        presum = [nums[0]]
        idx = 0
        n = len(nums)
        mindiff = inf
        flag = False
        for i in range(1,len(nums)):
            presum.append(presum[-1] + nums[i])

        for i in range(len(presum)-1):
 
            diff = abs((presum[i]//(i+1)) - ((presum[-1]- presum[i])//(n - (i+1))))
            if diff < mindiff:
                mindiff = diff
                idx = i
                flag = True
        if flag:
            i+=1
            diff = abs((presum[i]//(i+1)) - ((presum[-1]- presum[i])//n ))
            if diff < mindiff:
                mindiff = diff
                idx = i
        return idx