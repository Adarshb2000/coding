from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]):
        self.nums = nums
        self.multipliers = multipliers
        self.dp = {}
        return self.recur(0, 0, len(self.nums) - 1)

    def recur(self, i, start, end):
        if i == len(self.multipliers):
            return 0

        elif (i, start, end) not in self.dp:
            self.dp[(i, start, end)] = max(self.recur(i + 1, start + 1, end) + self.nums[start] * self.multipliers[i], self.recur(i + 1, start, end - 1) + self.nums[end] * self.multipliers[i])


        return self.dp[(i, start, end)]


print(Solution().maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))
