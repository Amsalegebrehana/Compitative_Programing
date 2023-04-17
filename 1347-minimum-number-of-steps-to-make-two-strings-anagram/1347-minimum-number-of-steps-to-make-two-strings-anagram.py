class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counters = defaultdict(int)
        countert = defaultdict(int)
        for i in range(len(s)):
            counters[s[i]] += 1
            countert[t[i]] += 1
   
        steps = 0
        
        for ch in countert:
          
            if counters[ch] < countert[ch]:
                steps += abs(counters[ch] - countert[ch])
            
        return steps
                
            