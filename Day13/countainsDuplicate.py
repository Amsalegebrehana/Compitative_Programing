#leetcode Contains Duplicates 217 solution

def containsDuplicates(nums):
    numsSet = set(nums)
    
    print(len(numsSet))
    numsSet = set(nums)
    if len(numsSet) - len(nums) != 0:
        return True
    else:
        return False
        # print(len(numsSet) - len(nums))


print(containsDuplicates([1,2,3,1]))