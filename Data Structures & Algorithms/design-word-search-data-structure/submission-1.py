class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            
            curr = curr.children[s]
        
        curr.word = True        

    def search(self, word: str) -> bool:
        curr = self.root
        for (index,s) in enumerate(word):
            if s != '.':
                if s not in curr.children:
                    return False
            else:
                return self.searchAtDot(word[index+1:],curr)
            
            curr = curr.children[s]
        
        return curr.word

            
    def searchAtDot(self,word,curr):
        if(len(word) == 0):
            for child in curr.children.values():
                if(child.word == True):
                    return True
            return False

        for node in curr.children.values():
            curr = node
            for (index,s) in enumerate(word):
                if s != '.':
                    if s not in curr.children:
                        break
                    else:
                        if(index == len(word) - 1 and curr.children[s].word):
                            return True                     
                else:
                    return self.searchAtDot(word[index+1:],curr)
                
                curr = curr.children[s]
                    
        return False
        


        
