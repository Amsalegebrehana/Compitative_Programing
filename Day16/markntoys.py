#hackerRank Mark and Toys solution 

def maxToys(prices, k):
    prices[:] = sorted(prices)
    print(prices)
    sum = 0
    c= 0
   
    for i in range(len(prices)):
        
        if sum + prices[i]  <= k:
            
            sum += prices[i] 
            c+=1
            
    return c
print(maxToys([1,12,5,111,200,1000,10],50))