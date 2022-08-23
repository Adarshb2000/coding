class Solution:
    def countVowelStrings(self, n: int):
        a = e = i = o = 1
        
        for _ in range(n):
            a, e, i, o = a + e + i + o + 1, e + i + o + 1, i + o + 1, o + 1
    
        return a