# leetcode Remove element solution 

def removeEle(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)
    
print(removeEle([3,2,2,3], 3))