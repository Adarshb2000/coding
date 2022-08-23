class Solution:
    def recur(self, i, j, word1, word2): 
        if i >= len(word1) and j < 0:
            return 0
        elif i >= len(word1) or j < 0:
            return 1
        
        if (i, j) in self.dp:
            return self.dp[(i, j)]

        i1 = i
        while i1 < len(word1) and word1[i1] != word2[j]:
            i1 += 1

        j1 = j
        while j1 >= 0 and word2[j1] != word1[i]:
            j1 -= 1
        
        self.dp[(i, j)] = max(self.recur(i1 + 1, j - 1, word1, word2) + 2 * int(i1 < len(word1)), self.recur(i + 1, j1 - 1, word1, word2) + 2 * int(j1 >= 0), self.recur(i + 1, j - 1, word1, word2))
        
        return self.dp[(i, j)]
            
    
    def longestPalindrome(self, word1: str, word2: str) -> int:
        self.dp = {}
        answer = self.recur(0, len(word2) - 1, word1, word2)
        return 0 if answer == 1 else answer
    
print(Solution().longestPalindrome('aa', 'ba'))
    
    