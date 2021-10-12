#leetcode two sum solution
def twoSum():
    nums = [3,2,4] 
    target = 6
    for i in range(len(nums)):
                for j in range(len(nums)):
                        
                        if nums[i] + nums[j] == target and i != j:
                            return i,j

print(twoSum())