from typing import List

class Solution:
    def dfs(self, i: int, j: int):
        if self.dp[i][j] != -1:
            return self.dp[i][j]
            
        self.dp[i][j] = 1
        if self.matrix[i][j + 1] > self.matrix[i][j]:
            self.dp[i][j] = max(self.dp[i][j], 1 + self.dfs(i, j + 1))
        
        if self.matrix[i][j - 1] > self.matrix[i][j]:
            self.dp[i][j] = max(self.dp[i][j], 1 + self.dfs(i, j - 1))

        if self.matrix[i + 1][j] > self.matrix[i][j]:
            self.dp[i][j] = max(self.dp[i][j], 1 + self.dfs(i + 1, j))

        if self.matrix[i - 1][j] > self.matrix[i][j]:
            self.dp[i][j] = max(self.dp[i][j], 1 + self.dfs(i - 1, j))

        return self.dp[i][j]
            
            
    def longestIncreasingPath(self, matrix: List[List[int]]):
        n = matrix.__len__()
        m = len(matrix[0])
        
        for i in range(n):
            matrix[i].append(0)
        
        matrix.append([0] * (m + 1))
        self.matrix = matrix
        self.dp = [[-1 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                self.dfs(i, j)
        
        ans = 0
        for i in range(n):
            ans = max(ans, max(self.dp[i]))
        
        return ans

print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))