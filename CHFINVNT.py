def chfinvnt(n, p, k):
    x = n % k
    temp = p % k
    c = -1 if temp - 1 == x else 0
    ans = (p // k) + 1 + c + temp * (n // k)
    return ans + temp if temp <= x else ans + x

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(chfinvnt(*map(int, input().split())))