# leet code Number of Good pair solution 
def numGoodPairs(nums):
    sum = 0 
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i< j:
                sum += 1

    return sum 
print(numGoodPairs([1,2,3]))
