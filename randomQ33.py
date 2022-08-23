dp = {}

def recur(problems: list[int], holidays: int):
    if len(problems) < holidays or not holidays:
        return False
    
    elif len(problems) == holidays:
        return sum(problems)
    
    elif (tuple(problems), holidays) in dp:
        return dp[(tuple(problems), holidays)]
    
    mini = 1e9
    for i in range(1, len(problems) - holidays + 1):
        ret = recur(problems[i :], holidays - 1)
        if ret is False:
            continue
        else:
            mini = min(ret, mini)
    
    dp[(tuple(problems), holidays)] = mini
    return mini

def solution(problems, holidays):
    ans = recur(problems, holidays)
    return -1 if ans is False or ans == 1e9 else ans

print(solution([1, 2, 3, 1, 2, 3, 1, 2, 3], 8))