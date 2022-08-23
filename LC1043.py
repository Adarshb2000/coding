from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int):
        self.dp = {}
        self.recur(0, arr, k)
        print(arr)
        print(list(self.dp[i] for i in range(len(arr))))
        return self.dp[0]
    
    def recur(self, i: int, numbers: List[int], k: int):
        if i >= len(numbers):
            return 0
        if i in self.dp:
            return self.dp[i]

        temp = -1
        
        for j in range(min(len(numbers) - i, k)):
            maxNum = max(numbers[i : i + j + 1])
            temp = max(temp, maxNum * (j + 1) + self.recur(i + j + 1, numbers, k))
        
        self.dp[i] = temp
        
        return self.dp[i]
    
print(Solution().maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3],4))