import heapq

def cf_702E(numbers: list):
    MIN = [(num, i) for i, num in enumerate(numbers)]
    heapq.heapify(MIN)

    answer = []

    for index, num in enumerate(numbers):
        mins = MIN.copy()
        while len(mins):
            curr, i = heapq.heappop(mins)
            if i == index:
                continue
            if curr > num:
                break
            num += curr
        else:
            answer.append(index + 1)
    
    print(len(answer))
    return answer
    

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        print(*cf_702E(list(map(int, input().split()))))