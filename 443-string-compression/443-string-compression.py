class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        i = 0
        j = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j+=1
            if j - i > 1 :
                result.append(chars[i])
                digit = str(j-i)
                for d in digit:
                    result.append(d)
            else:
                 result.append(chars[i])
            i = j
  
        chars[:]= result
        
                
                
        
        
        
        
        
        
        
        
       