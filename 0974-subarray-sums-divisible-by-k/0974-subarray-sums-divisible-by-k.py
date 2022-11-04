class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefsum = [0]
        for i in nums:
            prefsum.append(prefsum[-1] + i)
     
        for i in range(len(prefsum)):
            prefsum[i] = prefsum[i] % k
        
        dictt = defaultdict(int)
        result = [0] * len(prefsum)
        for i in range(len(prefsum)):
            if prefsum[i] in dictt:
                result[i] = dictt[prefsum[i]] 
            
            dictt[prefsum[i]] +=1
       
        return sum(result)
                
        