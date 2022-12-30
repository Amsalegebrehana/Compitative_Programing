class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        good = 0
        powers = [int(math.pow(2,i)) for i in range(22)]
        res = defaultdict(int)
      
        for i in range(len(deliciousness)):
            for j in powers:
           
                if j - deliciousness[i]  in res:
                    
                    good+= res[j- deliciousness[i]]
               
            res[ deliciousness[i]] +=1 
      
        return good % ((10 ** 9) + 7)
    
  