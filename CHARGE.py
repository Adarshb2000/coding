def getFactors(N: int = 10 ** 5):
    factors = [set() for _ in range(N + 1)]
    
    for n in range(2, N + 1):
        for i in range(1, int(n ** .5) + 1):
            if not n % i:
                factors[n].add(i)
                factors[n].add(n // i)
        factors[n].discard(n)
    return factors


if __name__ == '__main__':
    MAX = 10 ** 5
    factors = getFactors(MAX + 1)
    for T in range(int(input())):
        N = T
        print ('-' * 25, N, '-' * 25)
        answer = 0
        for b in range(2, N + 1):
            temp = 0
            for fact in factors[b]:
                x = (N - fact) // b + 1
                print(fact, x)
                temp += x
            answer += temp
        print('answer =', answer)
