def modeq(n, m):
    answer = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if ((m % a) % b) == ((m % b) % a):
                answer += 1
    
    return answer


if __name__ == '__main__':
    
    for _ in range(int(input())):
        n, m = map(int, input().split())
        print(modeq(n, m))