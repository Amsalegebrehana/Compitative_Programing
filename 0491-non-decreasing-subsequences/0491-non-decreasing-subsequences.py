class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
     
        def backtrack(i, path):
            
            if i == len(nums):
                if len(path) > 1:
                    result.add(tuple(path))
                return
            if path and path[-1] <= nums[i] or not path:

                path.append(nums[i])

                backtrack(i+1,path)

                path.pop()
            backtrack(i+1,path)
        backtrack(0,[])
  
        return result
     
        
                
                    
                