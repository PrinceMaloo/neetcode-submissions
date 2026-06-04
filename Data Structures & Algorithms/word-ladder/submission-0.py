class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjacent_list = defaultdict(list)
        words = [beginWord] + wordList

        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                word1 = words[i]
                word2 = words[j]
                if self.exactly_one_word_constraint(word1, word2):
                    adjacent_list[word1].append(word2)
                    adjacent_list[word2].append(word1)
                
        queue = deque()
        visit = set()
        queue.append((beginWord, 1))
        visit.add(beginWord)

        while queue:
            word, node_count = queue.popleft()

            if word == endWord:
                return node_count
            
            for next_word in adjacent_list[word]:
                if next_word not in visit:
                    queue.append((next_word, node_count + 1))
                    visit.add(next_word)
                     
        return 0
    
    def exactly_one_word_constraint(self, word1, word2):
        i = 0
        cnt = 0
        while(i < len(word1)):
            if word1[i] != word2[i]:
                cnt += 1

            i += 1
        
        if cnt == 1:
            return True
        
        return False

