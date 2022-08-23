def cf_734B(numbers: list, k: int):
    counts = {}
    answer = [0] * len(numbers)
    for index, num in enumerate(numbers):
        if num in counts:
            counts[num][0] += 1
            counts[num][1].append(index)
        
        else:
            counts[num] = [1, [index]]
        
    extras = []
    for count, indices in counts.values():
        if count >= k:
            for i in range(k):
                answer[indices[i]] = i + 1
        else:
            for i in indices:
                extras.append(i)
                
    
    while len(extras) >= k:
        for i in range(k):
            answer[extras.pop()] = i + 1
    
    return answer

if __name__ == '__main__':
    
    for _ in range(int(input())):
        _, k = map(int, input().split())
        print(*cf_734B(list(map(int, input().split())), k))