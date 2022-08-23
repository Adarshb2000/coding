n = 10 ** 5 + 1
primes = [0] * n
counts = [[0] * n for _ in range(5)]



def set_primes():
    
    for i in range(2, n):
        if not primes[i]:
            product = 1
            while i * product < n:
                primes[i * product] += 1
                product += 1

def set_counts():
    for i in range(5):
        for index, times in enumerate(primes[1 :], start=1):
            counts[i][index] = counts[i][index - 1] + int((i + 1) == times)
        
            

if __name__ == '__main__':
    set_primes()
    set_counts()
    
    for _ in range(int(input())):
        a, b, k = list(map(int, input().split()))
        print(counts[k - 1][b] - counts[k - 1][a - 1])

