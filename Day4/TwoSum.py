#leetcode two sum solution
def twoSum():
    nums = [3,2,3]
    target = 6
    #time complexity of O(n)
    for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                        
                        if nums[i] + nums[j] == target and i != j:
                            return i,j

    
    #time complexity of O(n2)

    for i in range(len(nums)):
                for j in range(len(nums)):
                        
                        if nums[i] + nums[j] == target and i != j:
                            return i,j

print(twoSum())