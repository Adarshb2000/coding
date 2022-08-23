from typing import List
from math import inf

class Solution:
    def minPathSum(self, grid: List[List[int]]):
        n = len(grid)
        m = len(grid[0])
        
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]
        
        for j in range(1, m):
            grid[0][j] += grid[0][j - 1]    
            
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        
        return grid[-1][-1]