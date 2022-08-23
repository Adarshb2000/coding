def checkValid(i, j, N, M):
    return 0 <= i < N and 0 <= j < M

visited = set()

def CanReach (N, M, Grid, x1, y1, x2, y2):
    matrix = Grid
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    
    if not matrix[x1][y1] % matrix[x2][y2]:
        print('YES')
        return
    
    numbers = set(matrix[x2][y2])



def recur(i, j, n, m, matrix, numbers, jumps):
    global visited
    if not checkValid(i, j, n, m):
        return False
    if (i, j) in visited: return False
    
    for num in numbers:
        if not matrix[i][j] % num:
            return True
    ans = False
    
    if jumps:
        ans = ans or recur(i - 1, j, n, m, matrix, numbers, jumps - 1)
        ans = ans or recur(i + 1, j, n, m, matrix, numbers, jumps - 1)
        ans = ans or recur(i, j - 1, n, m, matrix, numbers, jumps - 1)
        ans = ans or recur(i, j + 1, n, m, matrix, numbers, jumps - 1)
    
    return ans
        
    
    
        