class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        count = 0
        setofwords = set(words)
        memo ={}

        def checklength(word):
            count = 1
            if word not in memo:
      
                for i in range(len(word)):
                    temp = word[:i] + word[i+1:]

                    if temp in setofwords:
                        count = max(count, 1 + checklength(temp))
                memo[word] = count

            return memo[word]
     
        for word in words:
            count = max(count, checklength(word))
        return count