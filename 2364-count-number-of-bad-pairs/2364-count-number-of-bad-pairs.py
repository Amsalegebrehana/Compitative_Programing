class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = 0
        good = defaultdict(int)
        n = len(nums)
        allpairs = (n*(n-1))//2
       
        for i in range(n):
            count += good[nums[i] - i]
            good[nums[i] - i]+=1
       
        return allpairs - count