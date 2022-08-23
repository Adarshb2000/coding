def bittup(n, m):
    n = pow(2, n, MOD) - 1
    return pow(n, m, MOD)

if __name__ == '__main__':
    MOD = 10 ** 9 + 7
    for _ in range(int(input())):
        print(bittup(*map(int, input().split())))