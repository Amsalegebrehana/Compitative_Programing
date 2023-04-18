class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        opening = 0
        st = []
        moves = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                st.append(s[i])
                opening += 1
            elif s[i] == ")":
                if st:
                    st.pop()
                    opening -= 1
                else:
                    moves += 1
   
        return moves + opening