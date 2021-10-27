#selection sort

def selectionSort(nums):
    c=0
    for i in range(c , len(nums)):
        print("c", c)
        num = min(nums[c:])
        print(nums[c:])
        print("min ", num)
        numidx = nums.index(num)
        nums[c], nums[numidx] = nums[numidx],  nums[c]
        c+=1
    print(numidx)
   
    print(nums)
selectionSort([4,3,2,1,7])