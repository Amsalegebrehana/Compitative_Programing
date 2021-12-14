

def rearrangeArray(nums):
    l=[]
    nums[:]=sorted(nums)
    l=[]
    nums[:]=sorted(nums)
    for i in range(0, len(nums)-1):
        if i%2==0:
            nums[i], nums[i+1] = nums[i+1],nums[i]
    return nums
print(rearrangeArray([1,2,3,4,5]))