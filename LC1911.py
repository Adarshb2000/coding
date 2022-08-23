from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]):
        self.dp = {}
        return self.recur(0, 0, 1, nums)

    def recur(self, index, curr, turn, nums):
        if index == len(nums):
            return curr

        if (index, turn) not in self.dp:
            self.dp[(index,
                     turn)] = max(self.recur(index + 1, nums[index], 1, nums),
                                  self.recur(index + 1, 0, 1, nums))

        return self.dp[(index, turn)]


cases = [[4, 2, 5, 3], [5, 6, 7, 8], [6, 2, 1, 2, 4, 5]]
for case in cases:
    print(Solution().maxAlternatingSum(case))
