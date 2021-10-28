#leetcode rotate arr 189 solution 

def rotateArr(nums,k):
    
    k = k % len(nums)
    while k > 0:
        
        num = nums.pop()
        nums.insert(0, num)
        k -=1
    return nums
    


print(rotateArr([1,2],3))
print(rotateArr([-1,-100,3,99], 2))

