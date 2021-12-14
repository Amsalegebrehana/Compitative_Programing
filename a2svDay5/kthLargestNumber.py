

# leetcode kthLargestNumber solution

def kthLargestNumber(nums, k):
    
    l=[]
    for i in range(0,len(nums)):
       
        l.append(int(nums[i]))
    l=sorted(l)
    # l=l[::-1]
    print(l)
    
    return str(l[-k])
print(kthLargestNumber(["3","6","7","10"],4))
    