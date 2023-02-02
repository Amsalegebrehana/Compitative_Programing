class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = 0
        memo = {"0": 0,"1":0, "01":0, "10":0,"010":0,"101":0}
        
        for i in range(len(s)):
            if s[i] == "0":
                memo["0"] +=1
                memo["01"] += memo["1"]
                memo["010"] += memo["10"]
                
            else:
                memo["1"] +=1
                memo["10"] += memo["0"]
                memo["101"] += memo["01"]
        ways =  memo["101"]  + memo["010"] 
        
        return ways