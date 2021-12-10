#hackerrank Grading Students solution

def Grading(grades):
    l=[]
    n = grades[0]
    for i in range(1,n+1):
        # print(grades[i])
        if grades[i] >= 38:
            if grades[i] % 5 >= 3:
                grades[i] = grades[i] + (5-(grades[i]%5))
                l.append(grades[i])
            else:
                l.append(grades[i])
        else:
           l.append(grades[i])
        
        # l.append(grades[i])
        print(grades[i])
    return l
print(Grading([4,73,67,38,33]))