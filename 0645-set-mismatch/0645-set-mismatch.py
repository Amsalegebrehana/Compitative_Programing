class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numbers_freq = defaultdict(int)
        for i in nums:
            numbers_freq[i]+=1
        
        missing_num = -1
        dupulicate_num = -1
        for i in range(1,len(nums)+1):
            if numbers_freq[i]>1:
                dupulicate_num = i
            elif  numbers_freq[i] == 0 :
                missing_num=i
        return [dupulicate_num,missing_num]