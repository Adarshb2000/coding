from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int):
        self.ans = []
        self.numbers = sorted(candidates)
        self.target = target
        self.recur()
        return self.ans
    

    def recur(self, curr_index: int = 0, curr_nums: List[int] = [], curr_sum: int = 0):
        if curr_sum == self.target:
            self.ans.append(curr_nums)
            return
        
        if curr_index == len(self.numbers):
            return

        if curr_sum > self.target:
            return

        # Inclusive
        num = self.numbers[curr_index]
        temp = curr_nums.copy()
        temp.append(num)
        self.recur(curr_index + 1, temp, num + curr_sum)

        # Exclusive
        i = 0
        while curr_index + i < len(self.numbers) and self.numbers[curr_index + i] == self.numbers[curr_index]:
            i += 1
        self.recur(curr_index + i, curr_nums.copy(), curr_sum)
    
