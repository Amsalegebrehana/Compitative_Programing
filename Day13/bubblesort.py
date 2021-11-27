#Bubble sort solution

def bubbleSort(nums):
    for i in range(len(nums)):
        j = i
        while j < len(nums) :
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            j+=1
    return nums

print(bubbleSort([3, 1, 2, 4]))