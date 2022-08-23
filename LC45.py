from cmath import inf
from typing import List


class Solution:
    def jump(self, nums: List[int]):
        currMax = currLast = jumps = 0

        for index, num in enumerate(nums):

            currMax = max(currMax, num + currMax)

            if currMax >= len(nums) - 1:
                return jumps + 1
            
            if index == currLast:
                jumps += 1
                
    
print(Solution().jump([1,2,3]))
        
        