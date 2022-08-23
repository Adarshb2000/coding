def cf_753B(x: int, n: int):
    temp = 4 * (n // 4)
    r = n % 4
    if not r: 
        return x
    elif r == 1:
        return x + (temp + 1) if x % 2 else x - (temp + 1)
    elif r == 2:
        return x - 1 if x % 2 else x + 1
    else:
        return x - (temp + 4) if x % 2 else x + (temp + 4)
    
    
       

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(cf_753B(*map(int, input().split())))