#leetcode
def sortingsent(s):
    s1 = s.split(' ')
    r=''
    Dict = {}
    for i in s1:
        Dict[i[-1]] = i[:len(i)-1]
        #this will make the numbers key and the string value
    for i in range(1,len(s1)+1):
        r += Dict[str(i)] + ' '
        # i as a key to our dictionary then sort and put it to a string
        
    return r.strip()

print(sortingsent("is2 sentence4 This1 a3"))