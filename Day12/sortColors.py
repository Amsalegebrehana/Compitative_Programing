# leetcode Sort colors

def sortColors(nums):
    c = 0
    for i in range(c, len(nums)):
        # print(c)

        num = min(nums[c:])
        # print(nums)
        idx = nums.index(num)
        # print(idx)
        nums[c], nums[idx] = nums[idx], nums[c]
        c+=1
    return nums.reverse()

print(sortColors([2,0,2,1,1,0]))