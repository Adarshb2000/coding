from collections import deque

def cf_748C(numbers: list, n: int):
    queue = deque(sorted(numbers))
    answer = 0
    CAT = 0
    while len(queue):
        pos = queue.pop()
        answer += 1
        CAT += n - pos
        while len(queue) and queue[0] <= CAT:
            queue.popleft()
            
    return answer

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n, k = map(int, input().split())
        print(cf_748C(list(map(int, input().split())), n))