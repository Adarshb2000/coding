def delish(numbers):
    n = len(numbers)

    dp = [[0 for _ in range(n)] for _ in range(n)]
    max_ = numbers[0]
    min_ = numbers[0]

    for j in range(n):
        for i in range(j + 1):
            dp[i][j] += numbers[j] + dp[i][j - 1]
            if not (i == 0 and j == n - 1):
                if dp[i][j] > max_:
                    max_ = dp[i][j]
            if dp[i][j] < min_:
                min_ = dp[i][j]

    return max_ - min_



if __name__ == '__main__':
    
    # t = int(input())

    # while t:

    #     input()

    #     print(delish(list(map(int, input().split()))))

    #     t -= 1

    delish([-10, -9, 0, -6, -1, 3, 2, 2, -8, -7])