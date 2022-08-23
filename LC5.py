class Solution:
    def getLongestFromHere(self, string: str, index: int):
        i = j = index
        
        while j < len(string) and string[j] == string[i]:
            j += 1
        
        i -= 1
        
        while i >= 0 and j < len(string) and string[i] == string[j]:
            i -= 1
            j += 1
        
        return j - i - 1, string[i + 1: j]

    def longestPalindrome(self, s: str):
        maxLen = 0
        answer = ''
        for i in range(len(s)):
            length, string = self.getLongestFromHere(s, i)
            if length > maxLen:
                maxLen = length
                answer = string
            
        return answer
    
print(Solution().longestPalindrome('babad'))