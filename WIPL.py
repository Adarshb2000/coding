def recur(i: int = 0, height1: int = 0, height2: int = 0):
    if (i, height1, height2) in dp:
        return dp[(i, height1, height2)]
    elif (i, height2, height1) in dp:
        return dp[(i, height2, height1)]
    
    if height1 >= k and height2 >= k:
        return i
    
    elif i == n:
        return 1e9
    
    elif height1 >= k:
        return recur(i + 1, height1, height2 + numbers[i])
    
    elif height2 >= k:
        return recur(i + 1, height1 + numbers[i], height2)
    
    dp[(i, height1, height2)] = min(recur(i + 1, height1 + numbers[i], height2), recur(i + 1, height1, height2 + numbers[i]))
    return dp[(i, height1, height2)]




if __name__ == '__main__':
    for _ in range(int(input())):
        dp = {}
        n, k = map(int, input().split())
        numbers = sorted(list(map(int, input().split())), reverse=True)
        answer = recur()
        print(answer if answer != 10 ** 9 else -1)