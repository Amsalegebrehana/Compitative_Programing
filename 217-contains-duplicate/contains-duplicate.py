class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        freq_map = Counter(nums)

        for num in nums:
            if freq_map[num] > 1:
                return True
                
        return False
        