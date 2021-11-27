#hackerRank sWAP cASE solution

def sawpCase(s):
    str2 = ''
    for i in range(0, len(s)):
        if 65<= ord(s[i])<= 90:
            h = s[i].lower()
            str2 +=h
            
        else:
            x=s[i].upper()
            str2 +=x
           
            
    return str2
    
    
print(sawpCase("Pythonist 2"))