dp = {}
MOD = 10 ** 9 + 7

def solution(arr):
    if tuple(arr) in dp:
        return dp[tuple(arr)]
    
    if len(arr) == 2:
        return arr[0] * arr[1]
    
    temp = -1
    for i in range(len(arr) - 1):
        if len(arr) - 2 > i > 0:
            prod = arr[i - 1] * arr[i] * arr[i + 1] * arr[i + 2]
        elif i == len(arr) - 2:
            prod = arr[i - 1] * arr[i] * arr[i + 1]
        else:
            prod = arr[i] * arr[i + 1] * arr[i + 2]
        temp = max((solution(arr[: i] + arr[i + 2 :]) + prod) % MOD, temp)
    dp[tuple(arr)] = temp
    return temp
        

    
print(solution([1, 5]))