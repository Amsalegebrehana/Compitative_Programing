
def findRepeatedDnaSequences(s) :
    dictt = {}
    res = []
    for i in range(0,len(s)):
        
        if s[i:i+10] not in dictt and len(s[i:i+10]) == 10:
            dictt[s[i:i+10]] = 1
        elif s[i:i+10]  in dictt and len(s[i:i+10]) == 10:
                dictt[s[i:i+10]] += 1
    
    for i in dictt:
        if dictt[i] > 1:
            res.append(i)
    
    return res