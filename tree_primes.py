from collections import defaultdict as dd

def recur(i: int, last: bool):
    answer = 1
    for child in edges[i]:
        answer = (answer * (recur(child, True) + recur(child, False)) % MOD) % MOD
    
    answer += len(two_allowed) if last else len(primes)
    return answer
    
    
if __name__ == '__main__':
    MOD = int(1e9 + 7)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    two_allowed = [2, 7, 13, 19, 23, 31, 37, 43, 47, 53, 61, 67, 73, 79, 83, 89, 97]
    for _ in range(int(input())):
        N = int(input())
        edges = dd(list)
        for _ in range(N - 1):
            x, y = map(int, input().split())
            edges[x].append(y)
    
        print(recur(1, False))
            