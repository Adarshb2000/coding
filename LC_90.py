from typing import List

class Solution:
    def recur(self, numbers: List[int] = [], curr: int = 0):
        if curr == len(self.numbers):
            return
        
        # Inclusive
        temp = numbers.copy()
        temp.append(self.numbers[curr])
        self.answer.append(temp.copy())
        self.recur(temp, curr + 1)

        # Exclusive
        curr += 1
        while curr < len(self.numbers) and self.numbers[curr - 1] == self.numbers[curr]:
            curr += 1
        self.recur(numbers, curr)
        


    def subsetsWithDup(self, nums: List[int]):
        self.numbers = sorted(nums)
        self.answer = [[]]
        self.recur()
        return self.answer

print(Solution().subsetsWithDup([1, 2, 2]))
