def minTime(i: int, numbers: list, k: int, last: bool, slast: bool):
    if i == len(numbers) - 1:
        return numbers[i]
    
    elif not i:
        return minTime(i + 1, numbers, k, False, False) + numbers[i]
    
    if (i, last, slast) in dp:
        return dp[(i, last, slast)]
    
    if last and slast:
        dp[(i, last, slast)] = minTime(i + 1, numbers, k, False, True) + numbers[i]
    
    elif numbers[i] <= k:
        dp[(i, last, slast)] = minTime(i + 1, numbers, k, False, False) + numbers[i]

    else:
        dp[(i, last, slast)] = min(
            minTime(i + 1, numbers, k, True, last) + k,
            minTime(i + 1, numbers, k, False, last) + numbers[i],
        )
    
    if not last:
        dp[(i, last, not slast)] = dp[(i, last, slast)]
        
    return dp[(i, last, slast)]



if __name__ == '__main__':
    
    n = int(input())
    y = int(input())
    numbers = list(map(int, input().split()))
    
    dp = {}
    
    print(minTime(0, numbers, y, False, False))