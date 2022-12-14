class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        ans = []
        domaindcount = {}
        for domain in cpdomains:
      
            temp = domain.split(" ")

            temp2= temp[1].split(".")
   
            for i in range(len(temp2)):
                cur = ".".join(temp2[i:])
        
                if cur in domaindcount:
                    domaindcount[cur] +=int(temp[0])
                else:
                    domaindcount[cur] =int(temp[0])

        for i in domaindcount:
            res.append((domaindcount[i],i))

        res.sort()
        for i in res:
            ans.append(str(i[0])+ " " + i[1])
        return ans
                    
        