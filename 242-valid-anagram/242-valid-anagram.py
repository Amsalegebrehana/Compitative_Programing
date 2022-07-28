class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_Counter = Counter(s)
        
        t_Counter= Counter(t)
        
        return s_Counter==t_Counter