#leetcode missing number 

def missingNum(nums):
    n = len(nums) 
    for i in range(0, n+1):
        if i not in nums:
            return i 
        
        
print(missingNum([3,0,1]))
    