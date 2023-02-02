class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        result = []
        
        letterpair = []
        
        for i in range(len(logs)):
            temp = logs[i].split()
            temp = temp [1:]

            if temp[0].isdigit():
                digits.append(i)
            if not temp[0].isdigit():
                letters.append(i)
   
        for i in letters:
            temp = logs[i].split()
            f = temp[0]
            temp = temp [1:]
            temp = " ".join(temp)

            letterpair.append((temp, f, i))
            
        letterpair.sort()
       
        for i in range(len(letterpair)):
            result.append(logs[letterpair[i][2]])
        for i in digits:
            result.append(logs[i])
        return result