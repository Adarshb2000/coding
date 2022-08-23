from typing import List

class Solution:
    def solution(self, i, j):
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        x = self.numbers[i] + self.numbers[j]
        ans = 0 if x not in self.dict_ else 1 + self.solution(j, self.dict_[x]) 
        self.dp[i][j] = ans
        return ans
        
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        self.numbers = arr
        self.dict_ = {num: i for i, num in enumerate(arr)}
        self.dp = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        ans = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                ans = max(ans, 2 + self.solution(i, j))
            
        return ans

arr = [1,3,5]
print(Solution().lenLongestFibSubseq(arr))