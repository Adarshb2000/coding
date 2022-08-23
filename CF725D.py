from math import sqrt

def total_power(n):
    if n == 1:
        return 0
    answer = 0
    
    while not n % 2:
        answer += 1
        n //= 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while not n % i:
            answer += 1
            n //= i
    
    if n > 2:
        answer += 1
    
    return answer



def cf725D(a: int, b: int, k: int):
    if a == b and k == 1:
        return False
    return total_power(a) + total_power(b) >= k
        

if __name__ == '__main__':
    
    for _ in range(int(input())):
        a, b, k = map(int, input().split())

        print('Yes' if cf725D(a, b, k) else 'No')