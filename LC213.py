from typing import List


class Solution:
    def rob(self, nums: List[int]):
        return max(self.solve(nums[: -1]), self.solve(nums[1 :]))
    
    def solve(self, nums: List[int]):
        rob = [0] * len(nums)
        dont = [0] * len(nums)
        
        rob[0] = nums[0]
        
        for i in range(1, len(nums)):
            rob[i] = dont[i - 1] + nums[i]
            dont[i] = max(rob[i - 1], dont[i - 1])
        
        return max(rob[-1], dont[-1])

print(Solution().rob([2, 3, 2]))