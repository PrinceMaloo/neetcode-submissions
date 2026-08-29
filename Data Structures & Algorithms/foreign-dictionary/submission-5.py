from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        i, adjacency_list = 0, defaultdict(list)
        result, visit, loop = [], set(), set()
        unique = set()

        for word in words:
            for ch in word:
                unique.add(ch)

        while i < len(words) - 1:
            j, w1, w2 = 0, words[i], words[i+1]
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    adjacency_list[w1[j]].append(w2[j])
                    break
            
                j += 1
            
            if j == len(w2) and j != len(w1):
                return ""
            
            i += 1
        
        def dfs(node, loop):
            if node in loop:
                return True

            if node in visit:
                return False
            
            visit.add(node)
            loop.add(node)

            if node in adjacency_list:
                for neigh in adjacency_list[node]:
                    if dfs(neigh, loop):
                        return True
            
            result.append(node)
            loop.remove(node) 
            return False
        
  
        for node in adjacency_list:
            if dfs(node, loop):
                return ""
        
        result = result[::-1]
        for ch in unique:
            if ch not in visit:
                result.append(ch)

        return "".join(result)

            
            
        