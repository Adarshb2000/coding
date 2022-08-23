from collections import defaultdict as dd

from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

def firesc(start):
    visited[start] = True
    
    total = 1
    for i in matrix[start]: 
        if not visited[i]:
            total += firesc(i)

    return total

if __name__ == '__main__':
    MOD = 10 ** 9 + 7
    for _ in range(int(input())):
        n, m = map(int, input().split())

        matrix = dd(list)

        for _ in range(m):
            x, y = map(int, input().split())
            matrix[x - 1].append(y - 1)
            matrix[y - 1].append(x - 1)
        

        visited = [False] * (n)
        answer0 = 0
        answer1 = 1
        for i in range(n):
            if visited[i]:
                continue
            answer1 = (answer1 * firesc(i) % MOD) % MOD
            answer0 = (answer0 + 1) % MOD

        print(answer0, answer1)
