from string import ascii_lowercase


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]):
        from collections import defaultdict as dd
        from string import ascii_lowercase as letters
        wordList.append(beginWord)
        wordSet = set(wordList)
        if not endWord in wordSet:
            return 0

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
                    
        
        
        return self.BFS(beginWord, endWord)

    
    def BFS(self, startWord: str, endWord: str):
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


beginWord = "leet"
endWord = "code"
wordList = ["lest","leet","lose","code","lode","robe","lost"]
print(Solution().ladderLength(beginWord, endWord, wordList))
        
         
