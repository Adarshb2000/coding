def baseK(N: int, k: int):
    for num in range(N):
        n = num
        number = []
        while n:
            number.append(n % k)
            n //= k
        number.reverse()
        kits[num] = number
        

def xor(a, b, k):
    a: list = kits[a].copy()
    b: list = kits[b].copy()
    answer = i = 0
    while len(a) and len(b):
        x = (a.pop() + b.pop()) % k
        answer += (x) * (k ** i)
        i += 1
    
    while len(a):
        answer += a.pop() * (k ** i)
        i += 1
        
    while len(b):
        answer += b.pop() * (k ** i)
        i += 1    
    
    return answer
    
    
    
    

def cf_730D2(n: int, k: int):
    print(0, flush=True)
    if int(input()):
        return
    
    for i in range(1, n):
        query = xor(i, i - 1, k)
        print(query, flush=True)
        a = int(input())
        if a == 1:
            break
        elif a == -1:
            exit()
    else:
        exit()
            
        


if __name__ == '__main__':
    
    for _ in range(int(input())):    
        kits = {}
        n, k = map(int, input().split())
        baseK(n, k)
        kits[0] = [0]
        cf_730D2(n, k)