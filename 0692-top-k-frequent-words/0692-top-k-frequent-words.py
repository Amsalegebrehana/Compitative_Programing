class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        heap = []
        freq = Counter(words)
        
        for word in freq:
            heappush(heap, (-freq[word],word))
            
        while k > 0:
            result.append(heappop(heap)[1])
            k-=1
            
        return result
        