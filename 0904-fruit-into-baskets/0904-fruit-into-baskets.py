class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        left = 0
        ans = 0
        for r in range(len(fruits)):
            window[fruits[r]] +=1
            while len(window) > 2:
                window[fruits[left]] -=1
                ans = max(r - left, ans)
                if window[fruits[left]] == 0:
                    del window[fruits[left]] 
                left +=1
        ans = max(r - left + 1, ans)
        return ans
                    


            