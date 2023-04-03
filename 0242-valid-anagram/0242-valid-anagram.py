class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counters = Counter(s)
        countert = Counter(t)

        for i in counters:
            if countert[i] != counters[i]:
                return False
        for i in countert:
            if countert[i] != counters[i]:
                return False
        return True