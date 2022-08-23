def processQuery(n, p, query: list):
    answer = {
        'A': set(range(1, n + 1)),
        'B': set(),
        'C': set(),
        'D': set(),
        'E': set(),
    }
    query.sort()
    for q in query:
        start, process = q.split()
        process = int(process)
        if process in answer[start[0]]:
            answer[start[0]].remove(process)
            answer[start[1]].add(process)
    
    for key, value in answer.items():
        print(key, *sorted(value))


if __name__ == '__main__':
    
    n, s = map(int, input().split())
    query = []
    for _ in range(s):
        query.append(input())
        
    processQuery(n, p=s, query=query)