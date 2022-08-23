def recur(arr: list, t: int):
    global dp
    if t < 0 or t >= len(arr) or dp[t]:
        return False
    
    if not arr[t]:
        return True
    
    
    dp[t] = True
    return recur(arr, t + arr[t]) or recur(arr, t - arr[t])

def possiblerotation(n: int, arr: list, s: int):
    global dp
    dp = [False] * n
    t = arr.index(s)
    return recur(arr, t)


if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = 5
        numbers = [4, 2, 0, 2, 3]
        s = 4
        print(possiblerotation(n, numbers, s))