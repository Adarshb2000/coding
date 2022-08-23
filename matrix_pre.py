def prodSumMat(matA, maxK):
    n = len(matA)
    m = len(matA[0])
    
    matrix = [[1 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[i][j] = matA[i - 1][j - 1]
        
    
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            matrix[i][j] = matrix[i][j - 1] * matrix[i][j]
            if matrix[i][j] < 0:
                matrix[i][j] = -1
            elif matrix[i][j] > maxK:
                matrix[i][j] = -1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[i][j] = matrix[i - 1][j] * matrix[i][j]
            if matrix[i][j] < 0:
                matrix[i][j] = -1
            elif matrix[i][j] > maxK:
                matrix[i][j] = -1
    
    answer = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j] < 0:
                break
            else:
                answer += 1
    
    return answer
    