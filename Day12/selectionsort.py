#selection sort
#Built int minimum value
def selectionSort(nums):
    c=0
    for i in range(c , len(nums)):
       
        num = min(nums[c:])
       
        numidx = nums.index(num)
        nums[c], nums[numidx] = nums[numidx],  nums[c]
        c+=1
   
    print(nums)
selectionSort([4,3,2,1,7])


#custom min value
def selectionSortt(nums):
    for i in range(len(nums)):
        minNum = nums[i]
        print(minNum)
        for j in range(i+1, len(nums)):
            if minNum >= nums[j]:
                minNum = nums[j]
                print(minNum)


       
        idx = nums.index(minNum)
        print(idx)

        nums[i], nums[idx] = nums[idx], nums[i]
    return nums
   
print(selectionSortt([2,0,2,1,1,0]))