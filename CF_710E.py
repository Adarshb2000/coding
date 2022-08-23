def cf_710E(n: int, numbers: list):
    const = [None] * n
    temp = set()

    for index, num in enumerate(numbers):
        if num not in temp:
            const[index] = num
            temp.add(num)
        
    remainig = sorted(set(range(1, n + 1)).difference(temp))
    
    if not len(remainig):
        print(*const)
        print(*const)
        return
    
    # Creating MIN
    i = 0
    MIN = const.copy()
    for index, val in enumerate(MIN):
        if val is None:
            MIN[index] = remainig[i]
            i += 1
    
    # Creating MAX
    MAX = const.copy()
    currMax = -1
    for index, val in enumerate(MAX):
        if val is not None:
            currMax = val
            continue
        
        x = lowerBound(remainig, currMax)
        MAX[index] = remainig.pop(x)
    
    print(*MIN)
    print(*MAX)
        

def lowerBound(arr: list, element: int):
    answer = -1
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < element:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
        
    return answer
        
if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        cf_710E(n, list(map(int, input().split())))