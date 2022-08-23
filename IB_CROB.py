class Solution:
    def solve(self, A):
        self.n = len(A)
        self.m = len(A[0])
        
        for i in range(self.n):
            A[i].append(1)
        
        A.append([1] * (self.m + 1))
        
        self.visited = [[False for _ in range(self.m)] for _ in range(self.n)]
        self.matrix = A
        
        for i in range(self.n):
            if self.matrix[i][0] == 'O' and not self.visited[i][0]:
                self.dfs(i, 0)
            if self.matrix[i][self.m - 1] == 'O' and not self.visited[i][self.m - 1]:
                self.dfs(i, self.m - 1)
        
        for j in range(self.m):
            if self.matrix[0][j] == 'O' and not self.visited[0][j]:
                self.dfs(0, j)
            if self.matrix[self.n - 1][j] == 'O' and not self.visited[self.n - 1][j]:
                self.dfs(self.n - 1, j)
        
        
        for i in range(self.n):
            for j in range(self.m):
                A[i][j] = 'O' if self.visited[i][j] else 'X'
            A[i].pop()
        
        A.pop()
        
        return A
        
    
    def dfs(self, i, j):
        self.visited[i][j] = True
        
        if self.matrix[i + 1][j] == 'O' and not self.visited[i + 1][j]:
            self.dfs(i + 1, j)
        if self.matrix[i - 1][j] == 'O' and not self.visited[i - 1][j]:
            self.dfs(i - 1, j)
        if self.matrix[i][j - 1] == 'O' and not self.visited[i][j - 1]:
            self.dfs(i, j - 1)
        if self.matrix[i][j + 1] == 'O' and not self.visited[i][j + 1]:
            self.dfs(i, j + 1)

# A = [
#     ['X', 'X', 'X'],
#     ['X', 'X', 'O'],
#     ['X', 'X', 'X'],
# ]
# print(Solution().solve(A))
    
    
# inp = [ "XOOOOOOX", "XXOOXOOX", "OXXOXOXX" ]
# A = list(map(list, inp))
# for row in A:
#     print(*row)
# print('-' * 20)

# ans = Solution().solve(A)
# for row in ans:
#     print(*row)