from typing import List

class Solution:
    def solution(self, nums: List[int], i: int, last: int, size: int):

        while i > -1 and nums[i] >= last:
            i -= 1
            
        if i == -1:
            return size

        else:
            # Inclusive
            if self.dp[i] != -1:
                inclusive = self.dp[i]
            else:
                inclusive = self.solution(nums, i - 1, nums[i], 1)
                self.dp[i] = inclusive

            # Exclusive
            exculsive = self.solution(nums, i - 1, last, size)

            return max(size + inclusive, exculsive)
            
    
    def lengthOfLIS(self, nums: List[int]):
        self.dp = [-1] * len(nums)

        answer = 0
        for index, num in reversed(list(enumerate(nums))):
            if self.dp[index] == -1:
                self.dp[index] = self.solution(nums, index - 1, num, 1)
            answer = max(answer, self.dp[index])


        return answer

    
numbers = [1,3,6,7,9,4,10,5,6]
print(Solution().lengthOfLIS(numbers))
            