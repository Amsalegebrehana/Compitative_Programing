class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
 
        pair = []
        for i in range(len(ages)):
            pair.append((ages[i], scores[i]))
        pair.sort()
        
        memo = [[-1 for _ in range(len(pair))] for _ in range(len(pair))]
        
        def dp(memo,prev, pair, i ):
            if i >= len(pair):
                return 0
            
            if memo[prev+1][i] != -1:
                return memo[prev+1][i]
            jump = dp(memo,prev, pair, i + 1)
            nojump = 0
            if prev == -1 or pair[i][1] >= pair[prev][1]:
                
                nojump = pair[i][1] + dp(memo, i , pair, i + 1)
            memo[prev+1][i] = max(jump, nojump)
                
            return memo[prev+1][i]
        
        return dp(memo, -1, pair, 0)