class Solution:
    def reverse_by_range(self, l, r, arr):

        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        k = k % len(nums)

        nums.reverse()
      
        # first half
        self.reverse_by_range(0,k-1,nums)
        # second half
        self.reverse_by_range(k,len(nums) - 1, nums)

