from math import sqrt
from typing import List


class Solution:
    def numSquarefulPerms(self, nums: List[int]):
        mask = (1 << len(nums)) - 1
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        self.nums = nums
        self.dp = {}
        answer = 0
        for index, num in enumerate(self.nums):
            answer += self.recur((1 << index) ^ mask, num)
        
        fact = [1]
        for i in range(1, 13):
            fact.append(fact[-1] * i)
        
        for val in counts.values():
            answer //= fact[val]
        
        return answer
    
    def recur(self, mask, last):
        if not mask:
            return 1
        
        elif (mask, last) in self.dp:
            return self.dp[(mask, last)]
        
        answer = 0
        
        for index, num in enumerate(self.nums):
            if not (1 << index) & mask or not sqrt(num + last).is_integer(): continue
            answer += self.recur(mask ^ (1 << index), num)
        
        self.dp[(mask, last)] = answer
        
        return answer
    
print(Solution().numSquarefulPerms([2, 2, 2, 2, 2, 2, 7]))
            