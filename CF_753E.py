def cf_753E(n: int, m: int, commands: list):
    x = 0
    y = 0
    maxX = -1
    minX = n
    maxY = -1
    minY = m
    
    for c in commands:
        if c == 'L':
            x -= 1
            minX = min(x, minX)
            if x == -n:
                break
        elif c == 'R':
            x += 1
            maxX = max(x, maxX)
            if x == n:
                break
        elif c == 'U':
            y += 1
            maxY = max(y, maxY)
            if y == m:
                break
        elif c == 'D':
            y -= 1
            minY = min(y, minY)
            if y == -m:
                break
            
    

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(*cf_753E(*map(int, input().split()), list(input())))