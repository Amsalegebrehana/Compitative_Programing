class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = defaultdict(int)
        window = defaultdict(int)
        match = 0
        res = []
        left , right = 0, 0
        for i in p:
            need[i] +=1
    
        while right < len(s):
            curr = s[right]
            if curr in need:
                window[curr] +=1
                if window[curr] == need[curr]:
                    match +=1
            while match == len(need):
                currl = s[left]
               
                if right - left + 1 == len(p):
                    res.append(left)
                if currl in need:
                    window[currl] -=1
                    if window[currl] < need[currl]:
                        match -=1
                left +=1
            right +=1
        return res
                    