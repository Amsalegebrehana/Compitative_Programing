class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numbers_freq = defaultdict(int)
        for i in nums:
            
            numbers_freq[i]+=1
        
        res = []
        for i in range(1,len(nums)+1):
            if numbers_freq[i]>1:
                res.append(i)
            
        for i in range(1,len(nums)+1):
            if  numbers_freq[i] == 0 :
                res.append(i)
        return res