class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        steps = 0
        queue = deque([(startGene,steps)])
        visited = {startGene}
        while queue:
            curr,steps = queue.pop()
            
            if curr == endGene:
                return steps
            
            for i in 'ACGT':
                for j in range(len(curr)):
                    new_gene = curr[:j] + i + curr[j+1:]
               
                    if new_gene not in visited and  new_gene in bank:
                        queue.append((new_gene, steps+1))
                        
                        visited.add(new_gene)
                       
                        
        return -1