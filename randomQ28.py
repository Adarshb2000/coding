def calculate_primes(n):
    primes = [True for _ in range(n)]
    x = 2
    while x < n:
        if primes[x]:
            y = x
            while y * x < n:
                primes[y * x] = False
                y += 1

        x += 1

    return [i for i in range(2, n) if primes[i]]

