class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital = 0
        for i in word:
            if i.isupper():
                capital+=1
      
        if capital == len(word) or capital == 1 and word[0].isupper() or capital == 0:
            return True
        return False