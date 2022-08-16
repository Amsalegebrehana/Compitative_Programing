class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = Node()
            curr = curr.children[index] 
        curr.end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            index =  ord(ch) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index] 
            
        return curr.end
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            index =  ord(ch) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index] 
            
        return True
    def searchPrefix(self, word):
        curr = self.root
        for i,ch in enumerate(word):
            index = ord(ch) - ord('a')
            if curr.children[index] == None:
                
                return word
            if curr.children[index].end:
                return word[:i+1]
            curr = curr.children[index]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        s = sentence.split()
        ans = []
        for ch in s:
         
            ans.append(trie.searchPrefix(ch))
        return ' '.join(ans)
            
            
            
        