def CF811A(start, alarms):
    answer = 48 * 60
    for time in alarms:
        if time - start >= 0:
            answer = min(answer, time - start)
    
    return divmod(answer, 60)

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n, h, m = map(int, input().split())
        start = h * 60 + m
        alarms = []
        for _ in range(n):
            h, m = map(int, input().split())
            alarms.append(h * 60 + m)
            alarms.append(24 * 60 + h * 60 + m)
        
        print(*CF811A(start, alarms))