class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        incoming = defaultdict(list)
        outgoing = defaultdict(list)
        v = set()
        for i,j in edges:
            v.add(i)
            v.add(j)
            incoming[i].append(j)
            outgoing[j].append(i)

        m= max(v)
        ans = []
        for i in range(1,m+1):
            ans.append((i,len(incoming[i])+len(outgoing[i])))
        heap = []
        for i in ans:
            heappush(heap,(-i[1],i[0]))
      
        return heappop(heap)[1]
            