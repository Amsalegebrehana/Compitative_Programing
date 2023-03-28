class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupnums = set()
        result = []
        for num in nums:
            if num not in dupnums:
                dupnums.add(num)
            else:
                result.append(num)
        return result