class Solution:
    def minAddToMakeValid(self, s: str):
        answer = 0
        brackets = 0
        for c in s:
            if c == '(':
                brackets += 1
            else:
                if not brackets:
                    answer += 1
                else:
                    brackets -= 1
        
        return answer + brackets

print(Solution().minAddToMakeValid())