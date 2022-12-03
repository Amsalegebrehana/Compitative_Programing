class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        result = defaultdict(int)
        temp = []
        visited = {id}
        queue = deque([id])
        l = 1
        
        while queue:
            size = len(queue)
            for _ in  range(size):
                curr = queue.popleft()
                for i in friends[curr]:
                    if i not in visited:
                        if l == level:
                            temp.append(i)
                           
                        queue.append(i)
                        visited.add(i)
            if l == level:
                break
            l +=1
 
        ans = []
        for f in temp:
            for m in watchedVideos[f]:
                result[m] +=1
        for i in result:
            ans.append((result[i], i))

        ans.sort()
 
        return [i[1] for i in ans]
        
                    
                