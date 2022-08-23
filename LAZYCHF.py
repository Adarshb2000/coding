def lazychf(x, m, d):
    return min(x * m, x + d)

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(lazychf(*map(int, input().split())))