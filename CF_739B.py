for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x = abs(b - a)
    total = x * 2
    if total < max([a, b, c]):
        print(-1)
        continue
    
    print(x + c if x + c <= total else abs(x - c))
    
    