class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = defaultdict(int)
        loosers = defaultdict(int)
        for i,j in matches:
            winner[i] +=1
            loosers[j] +=1
  
        winner_res = []
        looser_res = []
        for i in winner:
            if winner[i] >=1 and i not in loosers:
                winner_res.append(i)
                
        for i in loosers:
            if loosers[i] == 1:
                looser_res.append(i)
        winner_res.sort()
        looser_res.sort()
        return [winner_res,looser_res]