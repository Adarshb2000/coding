

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]):
        from collections import defaultdict as dd
        from string import ascii_lowercase as letters
        wordList.append(beginWord)
        wordSet = set(wordList)
        if not endWord in wordSet:
            return []

        wordList = list(wordSet)
        
    
        self.graph = dd(list)
        
        for word in wordList:
            for i in range(len(word)):
                for c in letters:
                    temp = list(word)
                    temp[i] = c
                    word1 = ''.join(temp)
                    if word1 in wordSet:
                        self.graph[word].append(word1)
                    
        self.answer = []
        self.minimum = self.get_len(beginWord, endWord)
        if not self.minimum: return []
        self.BFS(beginWord, endWord)
        return self.answer

    def get_len(self, startWord: str, endWord: str):
        from collections import deque
        queue = deque([(startWord, 1)])
        visited = set()
        
        while queue.__len__():
            word, curr = queue.popleft()
            
            
            for node in self.graph[word]:
                if node not in visited:
                    if node == endWord:
                        return curr + 1
                    queue.append((node, curr + 1))
                    visited.add(node)
        
        return 0

    
    def BFS(self, startWord: str, endWord: str):
        from collections import deque
        queue = deque([(startWord, 1, set(startWord))])
        
        while queue.__len__():
            word, curr, curr_set = queue.popleft()
            if curr >= self.minimum:
                continue
            
            elif word == endWord:
                self.answer.append(list(curr_set))
                continue
            
            for node in self.graph[word]:
                if node not in curr_set:
                    temp = curr_set.copy()
                    temp.add(node)
                    queue.append((node, curr + 1, temp))
                    

print(Solution().findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
