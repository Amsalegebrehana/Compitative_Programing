#leet code 35 search insert position solution

def searchInstPosition(nums, target):
    left = 0
    right = len(nums)-1
    l=[]
    while left <= right:
        mid = (left+right)//2
        l.append(mid)

        if target == nums[mid]:
            return mid 
        elif target < nums[mid]:
            right = mid -1
        elif target > nums[mid]:
            left = mid + 1
    return right + 1 
print(searchInstPosition([-1,0,3,5,9,12], 2))