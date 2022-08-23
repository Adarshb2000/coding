if __name__ == '__main__':
    
    for _ in range(int(input())):
        s = input()
        if len(s) % 2:
            print('NO')
            continue
        x = len(s) // 2
        for i in range(x):
            if s[i] != s[x + i]:
                print('NO')
                break
        else:
            print('YES')