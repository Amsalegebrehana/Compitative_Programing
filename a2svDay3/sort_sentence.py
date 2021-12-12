#leetcode sorting the sentence solution

#using buble sort algorithm
def sortSentence(s):
    s1 = s.split(' ')
    r= ''
    for i in range(0, len(s1)):
        for j in range(0, len(s1)):
            if s1[i][-1] < s1[j][-1]:
                s1[i], s1[j] = s1[j], s1[i]
            # print(s1[j][-1])
    for i in s1:
        r += i[:-1] + ' '
     
    return r.strip()
print(sortSentence("is2 sentence4 This1 a3"))

#using python dictionary
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