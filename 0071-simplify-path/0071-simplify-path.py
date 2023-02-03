class Solution:
    def simplifyPath(self, path: str) -> str:
        path_l = path.split("/")
       
        st = []
        for i in path_l:
            
            if i =="" or  i == ".":
                
                continue
                
            elif st and i == "..":
                st.pop()
            elif i != "..":
                st.append(i)
            
   
        return "/" + "/".join(st)