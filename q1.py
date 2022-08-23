import heapq

def q1(filesize: list):
    heapq.heapify(filesize)

    answer = 0

    while len(filesize) > 1:
        first = heapq.heappop(filesize)
        second = heapq.heappop(filesize)
        temp = first + second
        answer += temp
        heapq.heappush(filesize, temp)


    return answer


if __name__ == '__main__':
    
    print(q1(list(map(int, input().split()))))