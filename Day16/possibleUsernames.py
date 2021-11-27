

def possibleChanges(usernames):
    l=[]
   
    ans = []
    for i in usernames:
        for j in range(len(i)):
            c=j
            while c < len(i):
                
                if ord(i[j]) < ord(i[c]) :
                    print("j",ord(i[j]))
                    print("c",ord(i[c]))
                    ans = 'YES'
                    break
                    # if ans == 'YES':
                    #    l.append(ans)
                    #    break
                    
                   
               
                else :
                    ans = 'NO'
                    break
                c+=1
        l.append(ans)
          
    print(l)
possibleChanges(["foo", "baz", "bar"])           