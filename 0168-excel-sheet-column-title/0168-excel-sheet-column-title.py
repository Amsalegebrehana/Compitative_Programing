class Solution:
    def convertToTitle(self, num: int) -> str:
        
        excel = {i+1:chr(ord("a") + i) for i in range(26)}
       
        flag = False
        ans = ""
        while num > 26:
            temp = num % 26
            num = num // 26
           
            if temp > 0:
                ans += excel[temp].upper()
            else:
                ans += excel[26].upper()
                num -= 1
        
        ans += excel[num].upper() 
   
        return ans[::-1]
            
            