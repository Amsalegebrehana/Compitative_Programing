def add(l,l2):
    ll=""
    b=0
    d=len(str(l))-len(str(l2))
    if len(str(l)) == len(str(l2)):
        for i in range(len(str(l))-1,-1,-1):
            x=int(str(l)[i])+ int(str(l2)[i]) + b
            a=x%10
            b=x//10
            ll+=str(a)
        print(ll[::-1])
    elif len(str(l)) > len(str(l2)):
        
        for i in range(len(str(l))-1,-1,-1):
            x=int(str(l)[i])+ int((d*"0"+ str(l2))[i])+ b
            a=x%10
            b=x//10
            ll+=str(a)
        print(ll[::-1])
    elif len(str(l2)) > len(str(l)):
       
        for i in range(len(str(l2))-1,-1,-1):
            x=int(((-1 * d) *"0" + str(l))[i])+ int(str(l2)[i])+ b
            a=x%10
            b=x//10
            ll+=str(a)
            
        print(ll[::-1])
add(415,27)
