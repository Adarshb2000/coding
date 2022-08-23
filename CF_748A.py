if __name__ == '__main__':
    
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        
        print(max(0, max(b, c) + 1 - a), max(0, max(c, a) + 1 - b), max(0, max(a, b) + 1 - c))