#leetcode valid Palindrome phrase solution

def palindrome(s):
  
    # x = ''.join(s.split(' '))
    h=''.join(filter(str.isalnum, s)).lower()
    s2='' 
    for i in range(len(h)-1,-1,-1):
        s2 += h[i]
    print(s2)
    print(h)
    if s2 == h:
        return True 
    else:
        return False
   
    # return h
    

print(palindrome("hello"))