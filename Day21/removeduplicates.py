#leetcode 26 Remove duplicates from array solution 

def removeDuplicates(nums):
    nums[:] = sorted(set(nums))
    return nums
    
print(removeDuplicates([-1,0,0,0,0,3,3]))