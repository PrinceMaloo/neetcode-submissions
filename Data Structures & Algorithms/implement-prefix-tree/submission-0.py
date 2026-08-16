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
            
            if i == len(word) - 1:
                curr.children[ch].is_word = True

            curr = curr.children[ch]
            i += 1


    def search(self, word: str) -> bool:
        curr, i = self.root, 0
        while i < len(word):
            ch = word[i]
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]

            if i == len(word) - 1:
                return curr.is_word
            
            i += 1
        
        return False


    def startsWith(self, prefix: str) -> bool:
        curr, i = self.root, 0

        while i < len(prefix):
            ch = prefix[i]
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]

            i += 1
        
        return True
        
        