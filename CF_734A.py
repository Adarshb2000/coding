def cf_734A(n: int):
    if n % 3 == 2:
        n -= 2 
        return n - (n // 3) * 2, (n // 3) + 1
    else:
        return n - (n // 3) * 2, (n // 3)

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(*cf_734A(int(input())))