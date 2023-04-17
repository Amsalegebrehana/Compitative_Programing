class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsset = set()
        for num in nums:
            if num in numsset:
                return True
            numsset.add(num)
        return False