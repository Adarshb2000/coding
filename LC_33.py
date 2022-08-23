from typing import List


class Solution:
    def search(self, nums: List[int], target: int):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            condition = (nums[0] <= nums[mid]) ^ (nums[0] <= target )
            if nums[mid] > target:
                if condition:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if condition:
                    high = mid - 1
                else:
                    low = mid + 1
                    
        return -1
for i in range(8):
    print(Solution().search([4,5,6,7,0,1,2],i))