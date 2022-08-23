for _ in range(int(input())):
    n, l, r = map(int, input().split())
    numbers = (list(map(int, input().split())))
    answer = 0
    i = 0
    j = 0
    
    while i < n:
        while j < n and numbers[i] + numbers[j] <= l:
            j += 1
        
        answer += j - i
        i += 1
    
    print(answer)