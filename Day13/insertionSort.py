

def selectionSort(nums):
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
   
print(selectionSort([3,1,2]))