s = "148"
k = 3
sumt=0

rs = s * k
rsint = int(rs)
while rsint > 0:
    sumt += (rsint %10)
    rsint = rsint //10
print(sumt)
    
