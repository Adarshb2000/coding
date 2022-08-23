from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]):
        answer = 0
        last = (0, 0)
        for a, b in sorted(envelopes):
            if last[0] < a and last[1] < b:
                answer += 1
                last = (a, b)
            
        
        return answer
        
        