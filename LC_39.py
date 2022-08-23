class Solution:
    def combinationSum(self, candidates: list[int], target: int):
        self.ans = []
        self.numbers = candidates
        self.target = target
        self.recur()
        return self.ans
    

    def recur(self, curr_index: int = 0, curr_nums: list[int] = [], curr_sum: int = 0):
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
        self.recur(curr_index, temp, num + curr_sum)

        # Exclusive
        self.recur(curr_index + 1, curr_nums.copy(), curr_sum)

print(*Solution().combinationSum([2,7,6,3,5,1], 9))