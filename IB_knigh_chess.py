class Solution:
    def knight(self, A, B, C, D, E, F):
        self.n = A
        self.m = B
        return self.BFS((C, D), (E, F))
        
    def BFS(self, start, end):
        from collections import deque
        
        visited = [[-1 for _ in range(self.m)] for _ in range(self.n)]
        queue = deque([[start[0] - 1, start[1] - 1, 0]])
        while len(queue):
            x, y, moves = queue.popleft()
            
            
            if x == end[0] - 1 and y == end[1] - 1:
                return moves
            
            visited[x][y] = moves
            
            
            for i in [-1, 1]:
                for j in [-1, 1]:
                    if self.n > x + 2 * i >= 0 and self.m > y + j >= 0 and visited[x + 2 * i][y + j] == -1:
                        queue.append([x + 2 * i, y + j, moves + 1])
                    if self.n > x + i >= 0 and self.m > y + 2 * j >= 0 and visited[x + i][y + 2 * j] == -1:
                        queue.append([x + i, y + 2 * j, moves + 1])
        
        
        return -1
    
print(Solution().knight(384, 387, 106, 134, 210, 35))