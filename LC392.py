class Solution:
    def isSubsequence(self, s: str, t: str):
        i = 0
        for c in t: 
            if i == len(s):
                return True
            if c == s[i]:
                i += 1
            
        
        return False