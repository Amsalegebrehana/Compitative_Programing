#leetcode Maximum Number of Coins You Can Get 

def maxNumCoin(piles):
    
    piles.sort()
    m =0 
    while len(piles) >0:
       
        l=[piles[0],piles[-2],piles[-1]]
        print(l)
        m+=l[1]
        print(m)
        piles.remove(piles[0])
        piles.pop()
        piles.pop()
        l=[]
    return m 


print(maxNumCoin([9,8,7,6,5,1,2,3,4]))