class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        t = set(sentence)
       
        if len(sentence) < 26:
            return False
        for i in letters:
           
            if i not in t:
             
                return False
        return True
        
        