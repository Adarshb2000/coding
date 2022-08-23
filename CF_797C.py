def CF797C(starts, ends):
    curr = 0
    answer = []
    for start, end in zip(starts, ends):
        start = max(start, curr)
        answer.append(end - start)
        curr = end
    
    return answer
        


for _ in range(int(input())):
    input()
    print(*CF797C(list(map(int, input().split())), list(map(int, input().split()))))