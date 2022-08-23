from random import randint

def lower_bound(arr, low, high, element):
    if low == high:
        return low + 1 if low < len(arr) - 1 and arr[low + 1] == element else low
    
    mid = (low + high) // 2 + 1
    if arr[mid] < element:
        return lower_bound(arr, mid, high, element)
    else:
        return lower_bound(arr, low, mid - 1, element)

def upper_bound(arr, low, high, element):
    if low == high:
        return low - 1 if low and arr[low - 1] == element else low
    
    mid = (low + high) // 2
    
    if arr[mid] > element:
        return upper_bound(arr, low, mid, element)
    else:
        return upper_bound(arr, mid + 1, high, element)


def ctime(F, K, proctoring: dict):
    if K == 0: return True
    starts = sorted(proctoring.keys())
    ends = list(proctoring.values())
    ends.append(0)
    ends.sort()
    for time in ends:
        start = time
        end = start + K
        if end > F: continue
        index = upper_bound(ends, 0, len(ends) - 1, start + 1)
        if start < ends[index] < end:
            continue
        index = lower_bound(starts, 0, len(starts) - 1, end - 1)
        if start < starts[index] < end:
            continue
        while index > -1:
            if proctoring[starts[index]] >= end and starts[index] <= start:
                break
            index -= 1
        else:
            return True

    return False




def brute_code(F, K, proctoring):
    if not K: return True
    numbers = set(list(range(F)))
    for s, e in proctoring.items():
        for i in range(s, e):
            numbers.discard(i)
    
    for i in numbers:
        for j in range(i, i + K):
            if j not in numbers:
                break
        else:
            return True
    return False


def something():
    while True:
        N = randint(1, 5)
        F = randint(1, 10)
        K = randint(0, F)
        proctoring = {}
        for _ in range(N):
            s = randint(0, F)
            e = randint(s, F)
            proctoring[s] = e
        if not proctoring: continue
        try:
            answer0 = ctime(F, K, proctoring)
        except IndexError:
            print(N, F, K)
            print(proctoring)
        answer1 = brute_code(F, K, proctoring)
        if answer0 != answer1:
            print(answer0, answer1)
            print(F, K)
            print(proctoring)
            break
    exit()

if __name__ == '__main__':

    something()
    
    for _ in range(int(input())):
        N, K, F = map(int, input().split())
        proctoring = {}
        for _ in range(N):
            s, e = map(int, input().split())
            if s == e:
                continue
            proctoring[s] = max(proctoring.get(s, 0), e)
        
        print('YES' if ctime(F, K, proctoring) else 'NO')