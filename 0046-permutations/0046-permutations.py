class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def rec(newarr,path):
      
            if not newarr:
                result.append(list(path))
                return 
                 
            for i in range(len(newarr)):
                newarrc = newarr[:i] + newarr[i+1:]
              
                path.append(newarr[i])
                rec(newarrc,path)
                path.pop()
                
        rec(nums, []) 
        return result
            