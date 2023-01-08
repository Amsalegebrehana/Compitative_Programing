class Solution:
    def longestWord(self, words: List[str]) -> str:

        currWord = ""
        words  = set(words)
        for word in words:
            j = len(word)
            while j > 0 :
               
                if word[:j] not in words:
                    break
                j -=1
            if j == 0 and len(currWord) < len(word):
                
                currWord = word
            elif j == 0 and len(currWord) == len(word):
                if currWord > word:
                    currWord = word
            
        return currWord
        
        
        
        