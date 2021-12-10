#codeforces Domino piling solution 

def dominoPilling(nums):
    
    product = int(nums[0]) * int(nums[1])
    result = product // 2
        
    return result


test_case = input()
nums = test_case.split(' ')
# m, n = map(int, input()).split())
print(dominoPilling(nums))
