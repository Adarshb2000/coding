def cf_710A(n: int, m: int, x: int):
    x -= 1
    coulumn = x // n
    row = x % n
    
    return row * m + coulumn + 1 


if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(cf_710A(*map(int, input().split())))