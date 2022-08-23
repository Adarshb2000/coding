from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]):
        nums.sort()
        counts = defaultdict(int)
        answer = set()
        for num in nums:
            counts[num] += 1
        
        for index, num in enumerate(nums):
            if num == 0:
                if counts[num] > 2:
                    answer.add((0, 0, 0))
                continue
            for i in range(index + 1, len(nums)):
                total = -(num + nums[i])
                if total in counts:
                    if total in [num, nums[i]] and counts[total] < 2:
                        continue
                    answer.add(tuple(sorted([num, nums[i], -num - nums[i]])))
        
        
        return [list(i) for i in answer]

print(Solution().threeSum([1,2,-2,-1]))