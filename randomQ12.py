def getDiff(numbers: list):
    numbers.sort(reverse=True)
    a = 0
    b = 0
    for i, num in enumerate(numbers):
        if not i % 2:
            a += num
        else:
            b += num
    
    return a - b


n = int(input())
numbers = list(map(int, input().split()))
print(getDiff(numbers))