class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(list(range(1,n+1)))
        i = 1
        while len(queue) > 1:
            curr = queue.popleft()
            if i == k:
                i = 1
            else:
                queue.append(curr)
                i +=1
        return queue[0]
        