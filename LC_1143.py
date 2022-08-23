class Solution:
    def solution(self, i: int = 0, j: int = 0):
        if i == self.n or j == self.m:
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if self.t1[i] == self.t2[j]:
            answer = 1 + self.solution(i + 1, j + 1)
        
        else:
            answer0 = self.solution(i, j + 1)
            answer1 = self.solution(i + 1, j)

            answer = max(answer0, answer1)
        
        self.dp[i][j] = answer
        return answer

    def longestCommonSubsequence(self, text1: str, text2: str):
        self.n = len(text1)
        self.m = len(text2)
        self.t1 = text1
        self.t2 = text2
        self.dp = [[-1 for _ in range(self.m)] for _ in range(self.n)]
        return self.solution()

t1 = 'abcde'
t2 = 'ace'
print(Solution().longestCommonSubsequence(t1, t2))