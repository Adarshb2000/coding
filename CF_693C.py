def longJumps(n: int, numbers: list):
    dp = [0] * n
    
    currMax = -1
    
    for index, num in enumerate(numbers):
        if index + num >= n:
            currMax = max(dp[index] + num, currMax)
        else:
            dp[index + num] = max(dp[index + num], dp[index] + num)
    
    return currMax

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        numbers = list(map(int, input().split()))
        
        print(longJumps(n, numbers))