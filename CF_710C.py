def LCS(s, t):
    n = len(s)
    m = len(t)
    dp = [[0 for i in range(m + 1)] for j in range(2)]
    res = 0
     
    for i in range(1,n + 1):
        for j in range(1,m + 1):
            if(s[i - 1] == t[j - 1]):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                if(dp[i % 2][j] > res):
                    res = dp[i % 2][j]
            else:
                dp[i % 2][j] = 0
    return res

def cf_710C(s: str, t: str):
    lcs = LCS(s, t)
    return len(s) + len(t) - 2 * lcs

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(cf_710C(input(), input()))