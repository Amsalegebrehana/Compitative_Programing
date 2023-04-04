class Solution:
    def decodeString(self, s: str) -> str:
        
        digits = []
        st = []
        nums = ""
        for ch in s:
            if ch == "[":
                if nums.isdigit():
                    digits.append(int(nums))
                nums = ""
                st.append(ch)
            elif ch == "]":
                temp = ""
                while st :
                    elm = st.pop()
                    if elm != "[":
                        temp = elm + temp
                    else:
                       
                        st.append(digits.pop() * temp)
                        temp = ""
                        break
            elif ch.isdigit():
                nums += ch 
     
            else:
                st.append(ch)
          
        return "".join(st)
            
                
        