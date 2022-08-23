class Solution:
    def lengthOfLongestSubstring(self, s: str):
        n = len(s)
        chars = set()
        i = 0
        max_length = 0
        length = 0
        while i < n:
            while i + length < n and s[i + length] not in chars:
                chars.add(s[i + length])
                length += 1
            
            max_length = max(max_length, length)

            if length + i == n:
                break

            while s[i] != s[i + length]:
                chars.remove(s[i])
                i += 1
                length -= 1
            
            i += 1
            
            
        return max_length

while True:
    print(Solution().lengthOfLongestSubstring(input()))