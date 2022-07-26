class Solution:
    def calculate(self, s: str) -> int:
        st= []
      
        curr = 0
        op = '+'
        
        opp = {'+','-','/','*'}
        for i in range(0,len(s)):
            ch = s[i]
            if ch.isdigit():
                curr = curr * 10 + int(ch) 
             
            if  ch in opp or i == len(s) -1:
                if op == "+":
                    st.append(curr)
                elif op == '-':
                    st.append(-1 * curr)
                elif op == '*':
                    st[-1] *= curr
                elif op == '/':
                     st[-1] = int(st[-1]/curr)
                curr = 0
                op=ch
        return sum(st)
                    
            