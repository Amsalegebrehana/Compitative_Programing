class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        currNode = self.root
        for ch in word:
            if ch not in currNode.children:
                currNode.children[ch] = TrieNode()
            currNode = currNode.children[ch]
            
        currNode.end = True
   
    def search(self, word):
        currNode = self.root
        for j, ch in enumerate(word):
            if ch not in currNode.children:
                return word
            elif currNode.children[ch].end:
                return word[:j+1]
            currNode = currNode.children[ch]
        return word
            

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentencel = sentence.split()

        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
        for i, word in enumerate(sentencel):
             sentencel[i] = trie.search(word)
                    
        print(sentencel)
        return " ".join(sentencel)