class Solution:
    def reverse_arr(self, l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        nums.reverse()
        # left half
        self.reverse_arr(0, k-1, nums)
        # right half
        self.reverse_arr(k, len(nums)-1, nums)
        