class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
   
        if numRows == 1:
            return result
       
       
        n = 2
        while n <= numRows:
            temp = [0 for i in range(n)]
            temp[0] = 1
            temp[-1] = 1
            for j in range(1,len(temp)-1):
                temp[j] = result[-1][j-1]+result[-1][j]
            result.append(temp)
            n+=1

        print(result)
        return result