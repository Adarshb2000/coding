class Solution:
    def black(self, A):
        A = list(map(list, A))
        self.n = len(A)
        self.m = len(A[0])
        
        for i in range(self.n):
            A[i].append('O')
        
        A.append(['O'] * (self.m + 1))
        
        self.A = A
        
        self.visited = [[False for _ in range(self.m)] for _ in range(self.n)]
        
        answer = 0
        for i in range(self.n):
            for j in range(self.m):
                if A[i][j] == 'X' and not self.visited[i][j]:
                    self.dfs(i, j)
                    answer += 1

        return answer
        
    def dfs(self, i, j):
        self.visited[i][j] = True
        
        if self.A[i - 1][j] == 'X' and not self.visited[i - 1][j]:
            self.dfs(i - 1, j)
        if self.A[i + 1][j] == 'X' and not self.visited[i + 1][j]:
            self.dfs(i + 1, j)
        if self.A[i][j - 1] == 'X' and not self.visited[i][j - 1]:
            self.dfs(i, j - 1)
        if self.A[i][j + 1] == 'X' and not self.visited[i][j + 1]:
            self.dfs(i, j + 1)