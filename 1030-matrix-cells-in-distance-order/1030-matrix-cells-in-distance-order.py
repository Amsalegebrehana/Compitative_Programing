class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        result= []
        heap = []
        for r in range(rows):
            for c in range(cols):
                dist = abs(rCenter - r) + abs(cCenter - c)
                heappush(heap,(dist,[r,c]))
     
        while heap:
            x = heappop(heap)
            result.append(x[1])
        return result
        