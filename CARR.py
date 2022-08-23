def recur(n: int, last: int = None, slast: int = None):
    global answer1
    if not n:
        answer1 += 1
        return
    
    for i in range(1, m + 1):
        if last == slast == i:
            continue
        recur(n - 1, i, last)
    

def matrixMultiplication(A, B):
    a = (((A[0][0] % MOD) * (B[0][0] % MOD)) % MOD) + (((A[0][1] % MOD) * (B[1][0] % MOD)) % MOD) % MOD
    b = (((A[0][0] % MOD) * (B[0][1] % MOD)) % MOD) + (((A[0][1] % MOD) * (B[1][1] % MOD)) % MOD) % MOD
    c = (((A[1][0] % MOD) * (B[0][0] % MOD)) % MOD) + (((A[1][1] % MOD) * (B[1][0] % MOD)) % MOD) % MOD
    d = (((A[1][0] % MOD) * (B[0][1] % MOD)) % MOD) + (((A[1][1] % MOD) * (B[1][1] % MOD)) % MOD) % MOD

    return [[a, b], [c, d]]

def carr(n, m):
    if n == 1:
        return m
    dp1 = m * (m - 1)
    dp2 = m
    for _ in range(2, n):
        temp = dp2
        dp2 = dp1
        dp1 = (((m - 1) % MOD) * ((dp1 + temp) % MOD)) % MOD
    
    return dp1 + dp2


if __name__ == '__main__':
    MOD = 1e9 + 7
    for m in range(1, 9):
        for n in range(1, m + 1):
            answer1 = 0
            # n, m = map(int, input().split())
            recur(n)
            answer0 = carr(n, m)

            if answer0 != answer1:
                print(n, m)
                print(answer0, answer1)
                break