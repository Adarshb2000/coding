def largestArea(samples):
    n = len(samples)
    m = len(samples[0])
    
    matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[i][j] = samples[i - 1][j - 1]
        
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[i][j] += matrix[i - 1][j]
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[i][j] += matrix[i][j - 1]
        
    
    for size in range(n, 1, -1):
        for i in range(n - size + 1):
            for j in range(n - size + 1):
                if matrix[i + size][j + size] - matrix[i][j] == size ** 2:
                    return size
    
    return 0

samples = [
    [0, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
]

print(largestArea(samples)) 