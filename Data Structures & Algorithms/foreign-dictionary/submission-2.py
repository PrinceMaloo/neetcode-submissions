class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c : set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_length = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""
            
            for j in range(min_length):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break
        
        visit = {}
        result = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nei in adj_list[c]:
                if dfs(nei):
                    return True
            
            visit[c] = False
            result.append(c)
            return False   

        for c in adj_list:
            if dfs(c):
                return ""
        
        result.reverse()
        return "".join(result)

