class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = defaultdict(set)
        unlocked = set()
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                keys[i].add(rooms[i][j])
                if rooms[i][j] != 0:
                    unlocked.add(rooms[i][j])

        queue = deque([0])
        visited = set()

        while queue:
            curr = queue.popleft()
            for nextkey in keys[curr]:
                if nextkey in unlocked:
                    unlocked.remove(nextkey)
                if nextkey not in visited:
                    queue.append(nextkey)
                    visited.add(nextkey)
      
        if unlocked:
            return False
        return True