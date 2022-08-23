from typing import List


class Solution:
    def maxProfit(self, prices: List[int]):
        currMin = 1e9
        answer = -1
        for price in prices:
            answer = max(answer, price - currMin)
            currMin = min(currMin, price)
        
        return answer