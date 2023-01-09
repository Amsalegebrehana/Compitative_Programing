class Solution:
    def decodeString(self, encode_string: str) -> str:
        st = []
        digits = []
        digit = ""
        for i in encode_string:
            if i.isdigit():
                digit +=i
            elif not i.isdigit():
                if digit:
                    digits.append(digit)
                digit = ""
                if i ==  "]":
                    temp = ""
                    while  st[-1] != "[":
                        temp = st.pop() + temp
                    st.pop()
                    if digits:
                        st.append(temp *int(digits.pop()))
                else:
                    st.append(i)
        return "".join(st)	
