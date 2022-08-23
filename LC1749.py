from cmath import inf
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]):
        return max(self.kadane(nums), self.kadane([-i for i in nums]))
    
    def kadane(self, nums: List[int]):
        curr = -inf
        MAX = -inf
        
        for num in nums:
            if curr + num < num:
                curr = 0
            
            curr += num
            MAX = max(curr, MAX)
        
        return MAX
                
        