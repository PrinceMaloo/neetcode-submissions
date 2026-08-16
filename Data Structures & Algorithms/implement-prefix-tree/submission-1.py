class TrieNode:
    def __init__(self, word = False):
        self.is_word = word
        self.children = {}


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr, i = self.root, 0
        while i < len(word):
            ch = word[i]
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]
            i += 1
        
        curr.is_word = True


    def search(self, word: str) -> bool:
        curr, i = self.root, 0
        while i < len(word):
            ch = word[i]
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]
            i += 1
        
        return curr.is_word


    def startsWith(self, prefix: str) -> bool:
        curr, i = self.root, 0

        while i < len(prefix):
            ch = prefix[i]
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]
            i += 1
        
        return True
        
        