#leetcode rotate arr 189 solution 

def rotateArr(nums,k):
    n = []
    print(nums[len(nums)-k])
    for i in range(len(nums)-k, len(nums)):
        n.append(nums[i])
        print(nums[i])
    # for i in range(k, 0,-1):
    #     num = nums[-1]
    #     nums.remove(num)
    #     nums.insert(0, num)

    h = nums[k+1:] + nums[:k+1]
    print(n)
    print(h)
    return nums


print(rotateArr([1,2,3,4,5,6,7],3))

