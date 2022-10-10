class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        pl = [i for i in palindrome]
        for i in range(len(pl)):
            if pl[i] != 'a':
                if i == len(pl)//2:
                    continue
                pl[i] = 'a'
                return "".join(pl)
            if pl[i] == 'a' and i == len(pl) -1:
                pl[i] = 'b'
        return "".join(pl)
            
                