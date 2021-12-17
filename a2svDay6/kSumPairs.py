# leetcode  K-Sum Pairs solution 

# nums.sort()
    # Dict={}
    # for i in nums:
    #     if k - i in nums:
    #         Dict[i] = k-i
    #         nums.remove(i)
    #         nums.remove(k-i)
            
    # # print(Dict)
    # # print(len(Dict))
    
    # # print(nums)
    # return len(Dict)
def  KSumPairs(nums,k):
    nums.sort()
    
    i = 0
    h=0
    j = len(nums) -1
    while i < j:
        if nums[i] + nums[j] == k:
           
            h+=1
            i+=1
            j-=1
            # nums.remove(nums[i])
            # nums.remove(nums[j])
        elif nums[i] + nums[j] < k:
            i+=1
        else:
            j-=1
    print(h)
    return h
            
print(KSumPairs([1,2,3,4],2))