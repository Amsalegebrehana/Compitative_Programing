class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs = Counter(t)
     
        left , right= 0, 0
        match = 0
        windows = defaultdict(int)
        res = float("inf"), None, None
        while right < len(s):
            curr = s[right]
            
            if curr in needs:
                windows[curr] +=1
                
                if windows[curr]  == needs[curr]:
                    match +=1
            
            while left <= right and match == len(needs):
                if right - left + 1 < res[0]:
                    res = ( right - left + 1, left, right)
                curleft = s[left]
                if curleft in needs:
                    windows[curleft] -=1
                    if windows[curleft] < needs[curleft]:
                        match -=1
                        
                left +=1
            
            right +=1
        
                
        return  "" if res[0] == float("inf") else s[res[1]:res[2]+1]
        