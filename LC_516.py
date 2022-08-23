class Solution:
    def solution(self, string: str, i: int, j: int):
        if i == len(string) or j < 0:
            return 0
        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if string[i] == string[j]:
            return 2 + self.solution(string, i + 1, j - 1)
        
        else:
            answer = max(self.solution(string, i, j - 1), self.solution(string, i + 1, j))
            self.dp[i][j] = answer
            return answer

    def longestPalindromeSubseq(self, s: str):
        self.dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return self.solution(s, 0, s.__len__() - 1)
        