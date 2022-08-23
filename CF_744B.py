from collections import deque

for _ in range(int(input())):
    n = int(input())
    numbers = deque(list(map(int, input().split())))
    answer = []
    for i in range(n - 1):
        elem = min(numbers)
        if numbers[0] == elem:
            numbers.popleft()
            continue
        j = 0
        while numbers[0] != elem:
            numbers.append(numbers.popleft())
            j += 1
        
        numbers.popleft()
        answer.append([i + 1, n, j])
    
    print(len(answer))
    for a in answer: print(*a)
