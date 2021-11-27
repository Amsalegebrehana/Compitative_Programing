#leetcode squares of sorted array 977
#insertion sort

def sortsqr(nums):
    n = []
    nums = [i**2 for i in nums]

    c = 0
    for i in range (c, len(nums)):
        num = min(nums)
       
        n.append(num)
        nums.remove(num)
       
        # nums[c]=num
  
    return n
print(sortsqr([1,3,1,2]))