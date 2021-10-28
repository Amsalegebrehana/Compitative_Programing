#leetCode merge sorted array 88 solution

def mergearr(nums1, m, nums2, n):
    
    nums1 = nums1[:m] + nums2[:n]
    
    nums3 = []  
    for i in range(len(nums1)):
        minNum = min(nums1)
        nums1.remove(minNum)
        nums3.append(minNum)
    nums1[:] = nums3
    return nums1

print(mergearr([1,2,3,0,0,0], 3, [2,5,6],3))