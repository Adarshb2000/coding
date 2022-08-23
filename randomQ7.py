from collections import deque


def BFS(matrix, word):
    starts = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == word[0]:
                starts.append((i, j, 0, ''))
    
    for start in starts:
        visited = [[False for _ in range(m)] for _ in range(n)]
        queue = deque([start])
        while len(queue):
            i, j, index, curr = queue.popleft()
            if not (0 <= i <= n and 0 <= j <= m):
                continue
            elif visited[i][j]:
                continue
            
            if matrix[i][j] == word[index]:
                index += 1
                curr += str(i + 1) + str(j + 1)
            else:
                continue
            
            visited[i][j] = True
            
            if index == len(word):
                return curr
            
            queue.append((i - 1, j, index, curr))
            queue.append((i + 1, j, index, curr))
            queue.append((i, j - 1, index, curr))
            queue.append((i, j + 1, index, curr))
            
    
    return -1

if __name__ == '__main__':
    
    n, word = input().split()
    matrix = []
    for _ in range(int(n)):
        matrix.append(list(input()))
    
    print(BFS(matrix, word))