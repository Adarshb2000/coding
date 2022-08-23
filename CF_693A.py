def powOf2(n: int):
    i = 0
    while not n % 2:
        i += 1
        n //= 2
    
    return i

for _ in range(int(input())):
    w, h, n = map(int, input().split())
    
    print("YES" if n <= 2 ** (powOf2(w) + powOf2(h)) else "NO")
    