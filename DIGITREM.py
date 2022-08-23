def digiterm(n: str, d: str):
    if d not in n:
        return 0
    if not int(d):
        if not int(n):
            return 1
        pos = n.find('0')
        return int('1' * (len(n) - pos)) + int(n[: pos]) * 10 ** (len(n) - pos) - int(n)
        

    pos = n.find(d)
    if not pos:
        return (int(n[0]) + 1) * 10 ** (len(n) - 1) - int(n)

    pos += int(d != '9')
    x = (int(n[ : pos]) + 1) * 10 ** (len(n) - pos)
    while d in str(x):
        x += (10 - int(d)) * 10 ** (len(n) - pos)

    return x - int(n)
    

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(digiterm(*input().split()))