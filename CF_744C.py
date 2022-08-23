def check(i, j, k, matrix):
    n = len(matrix)
    m = len(matrix[0])
    d = 0
    while i + d < n and j + d < m and j - d > -1:
        if matrix[i + d][j + d] == matrix[i + d][j - d]:
            if matrix[i + d][j + d]:
                d += 1
            else:
                break
        else:
            break
    
    d -= 1
    
    return d if d >= k else -1

def main():
    n, m, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    checked = [[0] * m for _ in range(n)]
    
    for i in range(n):
        s = input()
        for j, c in enumerate(s):
            if c == '*':
                checked[i][j] = matrix[i][j] = 1
                
    matrix.reverse()
    checked.reverse()
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j]:
                d = check(i, j, k, matrix)
                while d > -1:
                    checked[i + d][j + d] = checked[i + d][j - d] = 0
                    d -= 1
                
                

    for i in range(n):
        for j in range(m):
            if checked[i][j]:
                return False
    
    return True
                        

if __name__ == '__main__':
    for _ in range(int(input())):
        print('YES' if main() else 'NO')
    