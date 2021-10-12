#tution calculation rate 5% initial 10,000
this_year_tution = 10000 #given
rate = 0.05
count = 0
sum = 0
while count <= 10:
    #to calculate each year tution
    year_tution = count * this_year_tution * rate + this_year_tution
    
    count += 1
    if count <= 4:#to get the total tution for four years
        sum += year_tution
    
print(year_tution)
print(sum)

l=[1,1,1,2,2,3,4,5,5]
print(set(l))