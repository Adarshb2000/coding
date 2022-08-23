from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]):
        n = len(grid)
        trans = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                trans[i][j] = grid[j][i]
        
        rowMax = [max(row) for row in grid]
        colMax = [max(col) for col in trans]
        
        answer = 0
        for i in range(n):
            for j in range(n):
                answer += min(rowMax[i], colMax[j]) - grid[i][j]

        return answer
    
print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
        
        