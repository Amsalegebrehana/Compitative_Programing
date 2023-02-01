class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        p = day = 0
        pair = []
        for i in range(len(plantTime)):
            pair.append((growTime[i], plantTime[i] ))

        pair.sort()
        pair=pair[::-1]

        for i, j in pair:
            p += j
            day = max(day, p +i)
        return day
        