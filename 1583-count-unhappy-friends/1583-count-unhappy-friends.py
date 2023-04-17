class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
       
        unhappy_friend = 0
        pairs_store = {}

        for x, y in pairs:
            pairs_store[x] = y
            pairs_store[y] = x

        for x in range(n):
            y = pairs_store[x]

            for u in preferences[x]:
                v = pairs_store[u]
    
                if preferences[u].index(x) < preferences[u].index(v) and preferences[x].index(u) < preferences[x].index(y):
                    unhappy_friend+=1
                    break
        return unhappy_friend