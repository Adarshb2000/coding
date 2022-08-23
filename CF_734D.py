from random import randint

def cf_734D(n: int, m: int, k: int):
    if n == 1:
        return k == m // 2
    if m % 2:
        m -= 1
    if 2 * k > n * m:
        return False
    
    if (k / n).is_integer() and (k // n) <= m:
        return True
        
    return n % 2 == k % 2
    

# while True:
#     n = randint(1, 5)
#     m = randint(1, 5)
#     if n % 2 and m % 2:
#         if randint(0, 1):
#             n += 1
#         else:
#             m += 1
#     k = randint(1, (n * m) // 2)
    
#     print(n, m, k)
#     print(cf_734D(n, m, k))
#     input()


if __name__ == '__main__':
    
    for _ in range(int(input())):
        print('YES' if cf_734D(*map(int, input().split())) else 'NO')