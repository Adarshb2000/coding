def cf_710B(string: list, k: int):

    x = string.count('*')
    if not x:
        return 0
    if x == 1:
        return 1
    
    first = string.index('*')
    last = n - 1
    while string[last] != '*':
        last -= 1
    
    curr = first
    i = 2
    while True:
        if last - curr <= k:
            return i
        
        temp = min(n - 1, curr + k)
        
        while string[temp] != '*':
            temp -= 1
        
        i += 1
        curr = temp
    
    
    
    

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n, k = map(int, input().split())
        print(cf_710B(list(input()), k))