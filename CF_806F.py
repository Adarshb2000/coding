from functools import cmp_to_key

def func(a, b):
    if b[0] < min(a):
        return -1
    
    return 1

def CF806F(numbers):
    pairs = []
    for index, num in enumerate(numbers, start=1):
        if num < index:
            pairs.append([index, num])
    print(pairs)
    pairs.sort(key=cmp_to_key(func))
    
    return pairs

    


for _ in range(int(input())):
    input()
    print(CF806F(list(map(int, input().split()))))