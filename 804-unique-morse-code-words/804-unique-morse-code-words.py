class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letter_count = [chr(i+96) for i in range(1,27)]
      
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dictt = {}
        for i in range(len(letter_count)):
            dictt[letter_count[i]] = morseCode[i]
       
        result = set()
        for word in words:
            ans = ''
            for ch in word:
                ans += dictt[ch]
            result.add(ans)
        return len(result)