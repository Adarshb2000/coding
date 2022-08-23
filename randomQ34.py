from collections import defaultdict
from math import inf, isinf

def solution(arr, t, k):
    dp = defaultdict(lambda : inf)
    dp[0] = 0
    
    for time, score in arr:
        for key in list(dp):
            dp[key + score] = min(dp[key + score], dp[key] + time)
    
    answer = inf
    maxScore = -1
    for score, time in dp.items():
        if time > t:
            continue
        elif score > maxScore:
            maxScore = score
            answer = time
    
    if maxScore < k or answer > t:
        return -1
    return answer
    
print(solution([[1, 3], [5, 10], [3, 12]], 9, 10))