class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        freq_set = set()

        for num in nums:
            if num in freq_set:
                return True
            freq_set.add(num)
                
        return False
        