#leetcode median of two arrays 4 solution

def medianarr(nums1, nums2):
    nums1[:] = nums1 + nums2
    nums1[:] = sorted(nums1)

    if len(nums1) % 2 != 0:
        mid_idx = len(nums1) // 2
        median = nums1[mid_idx]
    elif len(nums1) % 2 == 0:
        mid_idx1 = len(nums1) // 2
        mid_idx2 = mid_idx1 -1
        print(mid_idx1)
        median = (nums1[mid_idx1] + nums1[mid_idx2])/ 2

    print(median)

    return nums1
print(medianarr([1,2], [3,4]))