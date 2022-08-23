# cook your dish here
def billards(n):
    if n == 1:
        return 0

    i = n % 2
    c = n // 2  - i

    fact = [1] * (c + i + 1)
    for a in range(1, c + i + 1):
        fact[a] = a * fact[a - 1]

    answer = 0
    while c >= 0:
        answer += fact[c + i] // (fact[c] * fact[i])
        c -= 3
        i += 2
    
    return answer % (10 ** 9 + 9)
        

if __name__ == '__main__':
    
    for _ in range(int(input())):
        for i in range(10):
            print(billards(int(input())))
        
        
    