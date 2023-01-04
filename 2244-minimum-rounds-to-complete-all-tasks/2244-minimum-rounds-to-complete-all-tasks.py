class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dictt = Counter(tasks)
        count =0
        
        for i in tasks:
            if  dictt[i] > 0:
                    
                if dictt[i] %3 == 0:
                    dictt[i] -= 3
                else:
                    dictt[i] -= 2
                   
                count+=1
        summ = sum(dictt.values())
    
        return count if summ == 0 else -1