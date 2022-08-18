class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
       
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
       
        result = set()
        for word in words:
            ans = ''
            for ch in word:
                ans += morseCode[ord(ch)-ord('a')]
            result.add(ans)
        return len(result)