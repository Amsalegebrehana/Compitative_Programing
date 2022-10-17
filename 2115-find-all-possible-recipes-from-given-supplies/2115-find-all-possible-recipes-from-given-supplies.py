class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        rin = defaultdict(set)
        incoming = defaultdict(int)
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                rin[ingredients[i][j]].add(recipes[i])
                
                incoming[recipes[i]] +=1
   
        res = []
        recipesset = set(recipes)
        queue = deque()
        for i in supplies:
            queue.append(i)
       
        while queue:
            curr = queue.popleft()
            if curr in recipesset:
                res.append(curr)
            for i in rin[curr]:
                incoming[i] -=1
                if incoming[i] == 0:
                    queue.append(i)
                    
        return res