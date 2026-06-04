class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.word = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        result = set()
        rows = len(board)
        cols = len(board[0])

        root = TrieNode()
        for word in words:
            root.add_word(word)
        


        def dfs(r, c, node, visit, current_word):            
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or board[r][c] not in node.children:
                return 

            visit.add((r,c))
            
            current_word += board[r][c]
            node = node.children[board[r][c]]

            if node.word:
                result.add(current_word)
   
            neighbours = [[0,1], [0,-1], [1,0], [-1,0]]

            for (dr, dc) in neighbours:
                nr = r + dr
                nc = c + dc
                dfs(nr,nc, node, visit,current_word)

            visit.remove((r,c))
        
        for i in range(rows):
            for j in range(cols):
                visit = set()
                dfs(i,j,root,visit,"")
            
        return list(result)


