class Solution:
    def findMin(self, nums: List[int]) -> int:
        minele = nums[0]
        for i in nums:
            if i < minele:
                minele = i
        return minele