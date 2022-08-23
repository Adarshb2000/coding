for _ in range(int(input())):
    n, q = map(int, input().split())
    hotels = []
    
    for _ in range(n):
        n, p, r = input().split()
        hotels.append((p, r, n))
    
    hotels.sort(key=lambda x: x[1])
    
    for _ in range(q):
        l, u = map(int, input().split())
        