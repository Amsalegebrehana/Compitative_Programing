#hackerrank repeated string solution

def reapetedStr(s,n):
    c=n-len(s)
    # if len(s) == 1 and s[0] == 'a':
    #     return n
    # while n > len(s)  :
    #     s +=s
    # s=s[:n] 
    l=[]
    for i in s:
        l.append(i)
    #     if i == 'a':
    #         c+=1
   
        
                
    print(l)
    print(c) 
     
    return s 
print(reapetedStr("aaa",10))