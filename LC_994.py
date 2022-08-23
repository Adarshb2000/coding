from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]):
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            grid[i].append(0)
        
        grid.append([0] * (m + 1))
        self.grid = grid

        self.answer = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.answer[i][j] = m * n
        
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    self.bfs(i, j)
        
        a = max(max(i) for i in self.answer)
        
        return -1 if a == m * n else a
                     
    def bfs(self, i, j):
        queue = deque([(i, j, 0)])
        
        while queue.__len__():
            i, j, count = queue.popleft()
            self.answer[i][j] = count
            
            if self.grid[i - 1][j] == 1:
                if self.answer[i - 1][j] > count + 1:
                    queue.append((i - 1, j, count + 1))
                
            if self.grid[i + 1][j] == 1:
                if self.answer[i + 1][j] > count + 1:
                    queue.append((i + 1, j, count + 1))

            if self.grid[i][j + 1] == 1:
                if self.answer[i][j + 1] > count + 1:
                    queue.append((i, j + 1, count + 1))
            
            if self.grid[i][j - 1] == 1:
                if self.answer[i][j - 1] > count + 1:
                    queue.append((i, j - 1, count + 1))
            