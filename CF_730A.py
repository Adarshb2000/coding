def cf_730A(a: int, b: int):
    
    diff = abs(b - a)
    if not diff:
        return diff, diff

    else:
        return diff, min(a - (a // diff) * diff, (a // diff + 1) * diff - a)
    


if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(*cf_730A(*map(int, input().split())))
    
    