from heapq import heappop, heappush

def cf_744D(numbers: list):
    heap = []
    for index, num in enumerate(numbers, start= 1):
        if num:
            heappush(heap, (-num, index))
        
    answer = []
    while len(heap) > 1:
        a, x = heappop(heap)
        b, y = heappop(heap)
        answer.append((x, y))
        if a + 1:
            heappush(heap, (a + 1, x))
        if b + 1:
            heappush(heap, (b + 1, y))
    return answer
if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        answer = cf_744D(list(map(int, input().split())))
        print(len(answer))
        for a in answer:
            print(*a)
        