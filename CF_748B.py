def cf_748B(n: int):
    if n < 25:
        return 10 ** 9
    answer = 0
    ends = {
        '0' : ['0', '5'],
        '5' : ['2', '7']
    }
    while n:
        while n % 10 not in [0, 5]:
            n //= 10
            answer += 1
        
        string = str(n)[:: -1]
        for i, c in enumerate(string[1 :]):
            if c in ends[string[0]]:
                return min(answer + i, answer + 1 + cf_748B(n // 10))
        n //= 10
        answer += 1
    return 10 ** 9 

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(cf_748B(int(input())))
            