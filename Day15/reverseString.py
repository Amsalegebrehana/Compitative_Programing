# leetcode 344 Reverse String recursion solution

def reverseString(s):
   
    j=0
    while j < len(s):
        last = s.pop()
       
        s.insert(j, last)
        j+=1
    # if s == []:
    #     return s
    # else: 
    #     reverseString(s[1:]) + s.append(s[0])
        
    return  s
print(reverseString(["h","e","l","l","o"]))