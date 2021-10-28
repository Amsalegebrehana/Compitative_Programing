#leetcode 283, move zeros solution

def moveZeros(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(i)
    return nums
print(moveZeros([0,1,0,3,12]))       