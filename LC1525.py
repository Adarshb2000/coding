class Solution:
    def numSplits(self, s: str):
        prefix = [set()]
        suffix = [set()]
        for c in s:
            temp = prefix[-1].copy()
            temp.add(c)
            prefix.append(temp)
        
        for c in reversed(s):
            temp = suffix[-1].copy()
            temp.add(c)
            suffix.append(temp)
        
        suffix.reverse()
        
        answer = 0
        for i in range(len(s)):
            if len(prefix[i]) == len(suffix[i]):
                answer += 1
        
        
        
        return answer

print(Solution().numSplits('aaaaa'))