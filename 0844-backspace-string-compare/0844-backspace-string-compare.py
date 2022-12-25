class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
  
        def helper(s):
            st1 = []
            for i in s:
                if st1 and i == "#":
                    st1.pop()
                elif  i != "#":
                    st1.append(i)
      
            return "".join(st1)
        sr = helper(s)
        tr = helper(t)
        return sr == tr