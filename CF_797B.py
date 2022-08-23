def CF797B(a, b):
    if len(a) == 1:
        return a[0] >= b[0]
    diff = 0
    for i, j in zip(a, b):
        if i and j:
            diff = i - j
            break
        
    for i, j in zip(a, b):
        if i < j:
            return False
        if j == 0 and diff >= i:
            continue
        if i - j not in [diff, 0]:
            return False
    
    return True

for _ in range(int(input())):
    input()
    print('YES' if CF797B(list(map(int, input().split())), list(map(int, input().split()))) else 'NO')