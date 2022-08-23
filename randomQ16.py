def processLogs(logs, threshold):
    counts = {}
    for s in logs:
        a, b, _ = s.split()
        counts[a] = counts.get(a, 0) + 1
        if a != b:
            counts[b] = counts.get(b, 0) + 1
        
    answer = []
    for key, value in counts.items():
        if value >= threshold:
            answer.append(int(key))
    
    answer.sort()
    
    return list(map(str, answer))


print(processLogs(['88 99 100', '88 99 200', '99 32 100', '12 12 15'], 2))