
#insertion sort

def insertionSort(n, nums):
    for i in range(1, len(nums)):
        current_val = nums[i]
        j = i- 1
        while j >=0 and current_val < nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1]=current_val
    return nums
    
        
print(insertionSort(4,[5, 7, 2, 4]))