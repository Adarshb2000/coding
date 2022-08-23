from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]):
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = len(nums) + 1
        
        for num in nums:
            x = abs(num)
            if x < len(nums) + 1 and nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                return i
        
        return len(nums) + 1
            
                
        
            
            
nums = [3, 4, -1, 1]
print(Solution().firstMissingPositive(nums))