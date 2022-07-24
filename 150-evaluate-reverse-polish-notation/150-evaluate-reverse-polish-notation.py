class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i == '+':
                st.append(st.pop() + st.pop())
            elif i == '-':
                st.append(-st.pop() + st.pop())
            elif i == '*':
                st.append(st.pop() * st.pop())
            elif i == '/':
                x = st.pop()
                st.append(int(st.pop()/x))
            else:
                st.append(int(i))
    
        return st[0]
                