def CF797D(numbers, k):
    whites = [0]
    for num in numbers:
        whites.append(whites[-1] + num)
        
    start = 0
    answer = k
    for start in range(len(numbers) - k + 1):
        answer = min(answer, whites[start + k] - whites[start])
        
    return max(answer, 0)
    
            


for _ in range(int(input())):
    _, k = map(int, input().split())
    print(CF797D(list(int(c == 'W') for c in input()), k))