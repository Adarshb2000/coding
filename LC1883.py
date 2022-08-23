from math import ceil, floor, inf, isinf
from typing import List


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int):
        self.speed = speed
        self.nums = dist
        self.dp = {}
        temp = self.recur(0, hoursBefore)
        for key, value in self.dp.items():
            if not isinf(value): print(key, value)
        return -1 if isinf(temp) else temp

    def recur(self, i, timeLeft: int):
        if timeLeft < 0:
            return inf

        elif i == len(self.nums):
            return 0
        
        if (i, timeLeft) not in self.dp:
            self.dp[(i, timeLeft)] = min(
            self.recur(i + 1, timeLeft - round(self.nums[i] / self.speed, 2)) + 1, 
            self.recur(i + 1, floor(timeLeft - self.nums[i] / self.speed)),
            )

        return self.dp[(i, timeLeft)]

print(Solution().minSkips([2,1,5,4,4,3,2,9,2,10]
,6
,7))