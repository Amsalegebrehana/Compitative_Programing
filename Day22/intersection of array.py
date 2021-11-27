#leetcode 349 Itersection of array solution

def intersection(nums1, nums2):
    inter_l = [] 
    for i in nums1:
        if i in nums2:
            inter_l.append(i) 
    inter_l[:] = list(set(inter_l) )      
    return inter_l
print(intersection([1,2,2,1],[6,7]))