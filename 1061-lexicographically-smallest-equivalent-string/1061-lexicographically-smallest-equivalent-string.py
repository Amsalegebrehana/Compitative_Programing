class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        letters = {chr(i):chr(i) for i in range(97,123)}
       
        
        def find(ch):
            if letters[ch] == ch:
                return ch
            
            letters[ch] = find(letters[ch])
            return letters[ch]
        
        def union(a,b):
            
            pa = find(a)
            pb = find(b)
         
            if pa != pb:
                if pa < pb:
                  
                    letters[pb] = pa
                else:
                    letters[pa] = pb
                
        for i in range(len(s1)):
            union(s1[i],s2[i])

        ans = ""
        for ch in baseStr:
            ans += find(letters[ch])
        return ans