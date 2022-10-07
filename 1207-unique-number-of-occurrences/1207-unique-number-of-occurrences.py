class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
     
        occurence = Counter(nums)
        sett = set()

        for i in occurence.values():
            if i in sett:
                return False
            sett.add(i)
        return True
            