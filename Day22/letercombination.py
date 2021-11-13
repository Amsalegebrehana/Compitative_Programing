#leetcode 17 letter combination of phone numbers solution 

def letter(digits):
    digits_dict = {
        '2':"abc", '3':"def", '4':"ghi", '5':"jkl",
        '6':"mno", '7':"pqrs", '8':"tuv",'9':"wxyz"
        }
    l=[]
    h='a'
    j = 'j'
    print(digits_dict.keys())
    l.append(h+j)
    return l
        
print(letter("digits"))