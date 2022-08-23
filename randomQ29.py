def SearchingChallenge(strArr):
    global visited
    matrix = []
    for string in strArr:
        matrix.append(list(map(int, string)))
        
    n = len(matrix)
    m = len(matrix[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            if not matrix[i][j] and not visited[i][j]:
                dfs(i, j, n, m, matrix)
                answer += 1
    
    return answer

visited = []

def dfs(i, j, n, m, matrix):
    global visited
    if not (0 <= i < n and 0 <= j < m):
        return
    
    if matrix[i][j] or visited[i][j]:
        return
    visited[i][j] = True
    dfs(i + 1, j, n, m, matrix)
    dfs(i - 1, j, n, m, matrix)
    dfs(i, j + 1, n, m, matrix)
    dfs(i, j - 1, n, m, matrix)
    

    
if __name__ == '__main__':
    strArr = []
    for _ in range(int(input())):
        strArr.append(input())
    print(SearchingChallenge(strArr))