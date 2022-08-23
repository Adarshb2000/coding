def recur(i: int, last: bool, slast: bool, times: int, n: int, m: int, k: int):
    global dp, MOD, x
    if i == m:
        return times
    
    if (i, last, slast) in dp:
        return dp[(i, last, slast)]
    
    temp = 0
    
    if last or slast:
        temp += recur(i + 1, False, last, times, n, m, k)
    
    temp += recur(i + 1, True, last, (times * x) % MOD, n, m, k)
    
    dp[(i, last, slast)] = temp % MOD
    return dp[(i, last, slast)]

def func(n, m, k):
    global dp, MOD, x
    dp = {}
    MOD = 10 ** 9 + 7
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (i * fact[i - 1]) % MOD
    x = 0
    for r in range(1, k + 1):
        x = (x + fact[n] // (fact[r] * fact[n - r])) % MOD

    recur(0, True, True, 1, n, m, k)
    return dp[(0, True, True)]


print(func(5, 5, 5))