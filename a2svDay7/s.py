


s= "abcacacac"
n = 2
l= len(s)
x = n%l
a =(abs(n-x))//l
r=''
if l == 1 and s[0] == 'a':
    print( n)
for i in range(a):
    r+=s
print(r)
if x !=0:
    r+=s[:x]
print(r)
print( r.count('a'))