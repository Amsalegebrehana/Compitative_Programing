#leetcode ThirdMaximumNumber solution 

def thirdMaximumNumber(nums):
    
    h=sorted(set(nums))
    
    if len(h)>=3:
        return h[-3]
        print( h[-3])
    else:
        return h[-(len(nums)-1)]
print(thirdMaximumNumber([0,-1,-1]))