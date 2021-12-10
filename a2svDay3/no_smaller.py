# leetcode how many number are smallest thatn the current number 
def smallerNums(nums):
    l = []
    for i in range(0, len(nums)):
        c = nums[i]
        count = 0
        for j in range(0, len(nums)):
            if  nums[j] < c:
               count +=1
        l.append(count)
            # print(nums[j])
    return l
                
print(smallerNums([8,1,2,2,3]))
    