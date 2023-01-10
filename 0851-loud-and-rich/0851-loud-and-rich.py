class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(set)
        result = defaultdict(set)
        incoming = defaultdict(int)
        answer = [i for i in range(len(quiet))]
        queue = deque([])
        for i , j in richer:
            graph[i].add(j)
            incoming[j] += 1

        for i in range(len(quiet)):
            if incoming[i] == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            for nebour in graph[curr]:
                result[nebour] = result[curr] |  result[nebour]
                result[nebour].add(curr)
                incoming[nebour]-=1
                if incoming[nebour] == 0:
                    queue.append(nebour)
       
        for i in range(len(quiet)):
            minquietness = (quiet[i],i)
            for j in result[i]:
                if quiet[j] < minquietness[0]:
                    minquietness = (quiet[j], j)
            if quiet[answer[i]] > minquietness[0]:
                answer[i] = minquietness[1]
        return answer
                
                