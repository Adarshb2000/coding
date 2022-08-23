for _ in range(int(input())):
    
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input())))
    
    answer = 0
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j] + matrix[j][~i] + matrix[~i][~j] + matrix[~j][i]
            
            answer += min(temp, 4 - temp)
        
    print(answer)