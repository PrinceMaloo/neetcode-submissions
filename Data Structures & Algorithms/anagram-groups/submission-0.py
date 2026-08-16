class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        visit = set()
        for (i, string) in enumerate(strs):
            if i in visit:
                continue
            sub_output = [string]
            visit.add(i)
            for j in range(i + 1, len(strs)):
                if self.isAnagram(string, strs[j]):
                    visit.add(j)
                    sub_output.append(strs[j])
            
            output.append(sub_output)
        
        return output

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        hash_map = defaultdict(int)
        for i in range(len(s)):
            hash_map[s[i]] += 1
            hash_map[t[i]] -= 1

        for ch in s:
            if hash_map[ch] != 0:
                return False
        
        return True

        