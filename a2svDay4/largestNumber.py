
from itertools import permutations
from typing import List
def largestNum(nums):
  
    s = ''
    for i in range(0, len(nums)):
        for j in range(len(nums)):
            if  str(nums[i])+str(nums[j]) < str(nums[j])+str(nums[i]):
            
                nums[i], nums[j] =nums[j], nums[i]
    # print(nums)
    for i in range(0, len(nums)):
        
        s += str(nums[i])
    s = str(int(s))
    # print(nums)
    return s

print(largestNum([0,0]))