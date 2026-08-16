
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            curr = curr.children[ch] 
        
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(curr, i):
            if i == len(word):
                return curr.is_word
            
            if word[i] != '.' and word[i] not in curr.children:
                return False
            
            if word[i] in curr.children:
                return dfs(curr.children[word[i]], i + 1)
            
            for child_trie_node in curr.children.values():
                if dfs(child_trie_node, i + 1):
                    return True
            
            return False

        return dfs(curr, 0)
            
        




        
