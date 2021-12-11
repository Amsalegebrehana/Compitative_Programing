



def sortc(nums):
    
    for i in range(0,len(nums)):
       for j in range(0,len(nums)):
        if nums[i] < nums[j] :
            nums[i] , nums[j] = nums[j], nums[i]
            
    # print(nums)
    return  nums   
print(sortc([0,2,1,2,0,0]))