from KAVGMAT import kavgmat as method0
from random import randint

def method1(n, m, matrix):
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
    
    # for i in range(n):
    #     print(*sum_matrix[i]);

    
    answer = 0

    square_sum = lambda x, y, size: sum_matrix[x][y] - sum_matrix[x][y - size] - sum_matrix[x - size][y] + sum_matrix[x - size][y - size] >= 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] >= 0:
                answer += 1
    
    for size in range(2, n + 1):
        for i in range(size, n + 1):
            for j in range(size, m + 1):
                if square_sum(i, j, size):
                    answer += 1
    
    # for size in range(1, n):
    #     for i in range(size, n):
    #         if :
    #             answer += m - size
    #             continue
    #         elif sum_matrix[]
    #         start = size
    #         end = m - 1
    #         while start < end:
    #             mid = (start + end) // 2
    #             if sum_matrix[i + 1][mid + 1] - sum_matrix[i + 1][mid - size] - sum_matrix[i - size][mid + 1] + sum_matrix[i - size][mid - size] < 0:
    #                 end = mid - 1
    #             else:
    #                 start = mid + 1
            
    #         print(start, end)

    return answer

if __name__ == '__main__':
    a = 0
    while True:
        n = randint(3, 100)
        m = randint(n, 1000)
        matrix = [[0 for _ in range(m)] for _ in range(n)]

        x = 0

        for j in range(m):
            x = randint(x, min([x + 10000, 10 ** 9]))
            matrix[0][j] = x
        
        x = matrix[0][0]

        for i in range(1, n):
            matrix[i][0] = x = randint(x, min([x + 10000, 10 ** 9])) 

        for i in range(1, n):
            for j in range(1, m):
                number = max([matrix[i - 1][j], matrix[i][j - 1]]) 
                matrix[i][j] = randint(number, min([number + 10000, 10 ** 9]))
        
        k = randint(0, 10 ** 9)

        new_matrix = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                new_matrix[-i][-j] = matrix[i - 1][j - 1] - k

        answer0 = method0(n, m, new_matrix)
        answer1 = method1(n, m, new_matrix)

        if answer0 != answer1:
            print(answer0, answer1)
            for i in range(n):
                print(*new_matrix[i])
            
            print(new_matrix)
            break
        else:
            print(a, "okay")
            a += 1