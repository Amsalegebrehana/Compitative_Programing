#leetcode valid parenthesis


def validPar(s):
    l=[]
    Dict = {'(':')', '{':'}','[':']'}
    if len(s) >=2:
        for i in s:
            # print(Dict[-1])
            if i in Dict:
                l.append(i)
            else:
                if l and  i == Dict[l[-1]] :
                    l.pop()
        
        if len(l) == 0:
            return True
        else: 
            return False     
    else:
        return False
    
print(validPar('()'))
       