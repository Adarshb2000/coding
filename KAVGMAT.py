def kavgmat(n, m, matrix):    

    sum_matrix = [[0 for _ in range(m)] for _ in range(n)]
    sum_matrix[0][0] = matrix[0][0]

    for i in range(1, m):
        sum_matrix[0][i] = sum_matrix[0][i - 1] + matrix[0][i]
    
    for i in range(1, n):
        sum_matrix[i][0] = sum_matrix[i - 1][0] + matrix[i][0]

    
    for i in range(1, n):
        for j in range(1, m):
            sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j - 1] + matrix[i][j] - sum_matrix[i - 1][j - 1]

    temp_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            temp_matrix[i][j] = sum_matrix[i - 1][j - 1]

    sum_matrix = temp_matrix
    
    
    answer = 0

    square_sum = lambda x, y, size: sum_matrix[x][y] - sum_matrix[x][y - size] - sum_matrix[x - size][y] + sum_matrix[x - size][y - size]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] >= 0:
                answer += 1
    
    for size in range(2, n + 1):
        for i in range(size, n + 1):
            if square_sum(i, size, size) < 0: continue
            elif not square_sum(i, -1, size) < 0: answer += m - size + 1; continue
            else:
                start = size
                end = m
                while start < end - 1:
                    mid = (start + end) // 2
                    if square_sum(i, mid, size) >= 0:
                        start = mid
                    
                    else:
                        end = mid
                answer += start - size + 1


    return answer



if __name__ == '__main__':
    # t = int(input())
    t = 1
    while t:

        # n, m, k = map(int, input().split())

        # matrix = [[None for _ in range(m)] for _ in range(n)]
        # for i in range(1, n + 1):
        #     matrix[-i] = [a - k for a in reversed(list(map(int, input().split())))]

        n = 3; m = 4

        matrix = [
            [20, 7, -3, -13],
            [11, 5, -9, -14],
            [4, -5, -16, -19]]

        print(kavgmat(n, m, matrix))


        t -= 1