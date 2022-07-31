class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        result = []
        num = set(nums)
        for i in num:
            if freq[i] == 1:
                if i - 1 in num or i + 1 in num:
                    continue
                result.append(i)
        return result