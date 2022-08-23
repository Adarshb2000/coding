import heapq

def maxProfit(numbers):
    heap = []
    answer = 0
    for num in numbers:
        if heap and heap[0][0] < num:
            answer += num - heap[0][0]
            if heap[0][1]:
                heap[0][1] = False
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, [num, True])
        else:
            heapq.heappush(heap, [num, False])
    
    return answer

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    
    print(maxProfit(numbers))
    