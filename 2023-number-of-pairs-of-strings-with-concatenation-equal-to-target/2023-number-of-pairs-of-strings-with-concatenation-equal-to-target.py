class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        result = 0
        
        for i in range(len(nums)):
            size_need =  len(target) - len(nums[i]) 
    
            for j in range(len(nums)):
                if i != j and len(nums[j]) == size_need:
                    if nums[i] + nums[j] == target:
                        result +=1
        return result