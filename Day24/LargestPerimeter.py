#leetcode largest Perimeter solution

def largestP(nums):
    l=[]
    nums[:] = sorted(nums)
    print(nums)
    print(nums[1:])
    
    
    for i in range(len(nums)-1, len(nums)-4, -1):
        l.append(nums[i])
    print(l)
    if l[-1] + l[-2] > l[0]:
        sum = l[0] +  l[-1] + l[-2]
        print(sum)
        return sum 
    else: 
        return 0
    # return l

print(largestP([3,6,2,3]))


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
l = Node(5)#this is creating an object
print(l.data)
for i in range(1,4):
    print((10**(i)//9)*i)
    # for j in range(0,i):
    #     print(i, end="")
    # print()