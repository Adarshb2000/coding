from collections import defaultdict as dd, deque

def cf_762E(n: int, numbers: list):
    answer = []
    minusOne = False
    future = 0

    counts = dd(int)
    for num in numbers:
        counts[num] += 1
        
    countg1 = []

    for i in range(n + 1):
        if minusOne:
            answer.append(-1)
            continue
        ans = 0
        
        if not counts[i]:
                
            if not len(countg1):
                answer.append(-1)
                minusOne = True
                continue
            else:
                temp = countg1.pop()
                counts[temp] -= 1
                if counts[temp] > 1:
                    countg1.append(temp)
                counts[i] += 1
                ans = i - temp
        answer.append(ans + counts[i] + future)
        if counts[i] > 1:
            countg1.append(i)
        future += ans
    return answer
        

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(*cf_762E(int(input()), list(map(int, input().split()))))
    