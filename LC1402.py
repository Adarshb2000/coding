from cmath import inf
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]):
        satisfaction.sort()
        answer = curr = 0

        while satisfaction and curr + satisfaction[-1] > 0:
            curr += satisfaction.pop()
            answer += curr
        
        return answer

print(Solution().maxSatisfaction([-1,-8,0,5,-7]))
        
        