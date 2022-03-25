class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            maxx = -float('inf')
            minn = float('inf')
            for j in range(i,len(nums)):
                maxx=max(maxx,nums[j])
               
                minn=min(minn,nums[j])
               
                ans += maxx-minn
        return ans
                