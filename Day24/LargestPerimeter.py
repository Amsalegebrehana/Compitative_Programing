#leetcode largest Perimeter solution

def largestP(nums):
    l=[]
    nums[:] = sorted(nums)
    print(nums)
    print(nums[1:])
    
    
    for i in range(len(nums)-1, len(nums)-4, -1):
        l.append(nums[i])
    print(l)
    if l[-1] + l[-2] > l[0]:
        sum = l[0] +  l[-1] + l[-2]
        print(sum)
        return sum 
    else: 
        return 0
    # return l

print(largestP([3,6,2,3]))
