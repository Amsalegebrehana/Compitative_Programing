#leetcode 167 Two Sum ll - Input Array Is sorted solution

def twoSum(numbers, target):
    left = 0
    l=[]
    right = len(numbers) -1
    while left < right:
        mid = (left + right )//2
        if target >= numbers[mid]:
            right = mid -1 
            numbers[:] = numbers[:mid+1] 
            numslen = len(numbers)
            c=0
            for i in range(numslen):
                if target - numbers[c] == numbers[i] and c < numslen and c!=i:
                    l.append(c)
                    l.append(i)
                    c+=1
      
    return numbers, numslen,l

print(twoSum([2,3,4],6))
                