class Solution:
    def minimumDeletions(self, s: str) -> int:
        bs = [] 
        aS = [] 
        b = a = 0
        st = [(s[0], 0)]
        for i in range(len(s)):
            bs.append(b)
            if s[i] == "b":
                b +=1
       
        for i in range(len(s) - 1, -1, -1):
            aS.append(a)
            if s[i] == "a":
                a +=1
        aS = aS[::-1]
   
        removed = inf
        for i in range(len(s)):
            removed = min(removed, aS[i] + bs[i]) 
        
        
        return removed
                    
                    
                
                
            
        