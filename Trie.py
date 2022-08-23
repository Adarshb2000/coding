class Trie:
    def __init__(self):
        self.trie = [[None, False] for _ in range(26)]
    
    def __getitem__(self, index):
        x = ord(index) - 97
        return self.trie[x]
    
    def __setitem__(self, index, val):
        x = ord(index) - 97
        self.trie[x] = val
    
    def addWord(self, word):
        curr = self
        
        for c in word[: -1]:
            if curr[c][0] is None:
                curr[c][0] = Trie()
            
            curr = curr[c][0]
        
        curr[word[-1]][1] = True
        
    def searchWord(self, word):
        curr = self
        
        for c in word[: -1]:
            if curr[c][0] is None:
                return False
            curr = curr[c][0]
            
        return curr[word[-1]][1]


wordList = set(['soumya', 'adarsh', 'aayat'])

trie = Trie()
for word in wordList:
    trie.addWord(word)
    
while True:
    print(trie.searchWord(input()))
    
    