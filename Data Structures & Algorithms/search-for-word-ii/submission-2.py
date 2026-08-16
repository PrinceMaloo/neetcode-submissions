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

class Solution:
    def __init__(self):
        self.prefix_tree = PrefixTree()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        visit = set()
        result = set()

        for word in words:
            self.prefix_tree.insert(word)

        def dfs(r, c, sub_result, curr):
            if min(r, c) < 0 or r >= rows or c >= cols or (r,c) in visit or board[r][c] not in curr.children:           
                return
            
            curr = curr.children[board[r][c]]
            sub_result += board[r][c]
            if curr.is_word:
                result.add(sub_result)
            
            neighbours = [[0,1], [0, -1], [1, 0], [-1, 0]]
            visit.add((r,c))
            for dr, dc in neighbours:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, sub_result, curr)
            
            visit.remove((r,c))
            return

        for r in range(rows):
            for c in range(cols):
                curr = self.prefix_tree.root
                dfs(r,c, "", curr)

        return list(result)


                
        