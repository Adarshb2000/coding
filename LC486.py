from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]):
        self.nums = nums
        self.states = {}
        return self.calculateState(0, len(nums) - 1, -1) > -1
        
    def calculateState(self, start, end, turn):

        turn *= -1
        
        if start == end:
            return self.nums[start] * turn
        
        if (start, end) not in self.states:
            self.states[(start, end)] = turn * max(
                turn * (self.calculateState(start + 1, end, turn) + self.nums[start] * turn),
                turn * (self.calculateState(start, end - 1, turn) + self.nums[end] * turn)
            )

        return self.states[(start, end)]

print(Solution().PredictTheWinner([1, 5, 225, 7]))
        