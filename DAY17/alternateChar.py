#hackerrank Alternating characters solution
 # c=0
    # ss=''
    # odd = 1
    # for i in range(len(s)):
    #     if i % 2 == 0:
    #         even = i
    #         print("even", even)
    #     if i % 2 != 0:
    #         odd = i
    #         print("odd",odd)
    #     while s[even]==s[odd]:
    #         print(s[even])
    #         print(s[odd])
    #         s=s.replace(s[even],'')
    #         c+=1 
    #         even +=1
    #         odd +=1
    # return c,s
            
            
def altChar(s):
    str2 = s[0]
   
    count = 0
  
    for i in range(0, len(s)):
        # if s[i] == str2[count]:
        #     result +=1
       if s[i] != str2[count]:
            str2+=s[i]
            count+=1
           
    x =  len(s) - len(str2)
    # print(abs(x))
    return abs(x)

   
print(altChar("AAAA"))