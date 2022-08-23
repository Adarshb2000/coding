from collections import defaultdict


def func(string):
    n = len(string)
    dp = [0] * (n + 2)
    dp[0] = 1
    SUM = [0] * (n + 2)
    last = defaultdict(lambda: -1)
    for i in range(n + 1):    
        dp[i] = SUM[i - 1] - SUM[last[string[i - 1]] - 1]
        SUM[i] = SUM[i - 1] + dp[i]
        last[string[i - 1]] =  i
        
    return SUM[n - 2]

print(func(input()))