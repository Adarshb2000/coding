def climbingScoreboard(s, scored, x, trial):
    res = [0] * x

    scores = [scored[0]]
    for num in scored:
        if scores[-1] != num:
            scores.append(num)

    currMax = -1
    for index, score in enumerate(trial):
        if score > currMax:
            res[index] = floor(scores, score) + 1
            currMax = score
        else:
            res[index] = res[index - 1]
    return res


def floor(arr: list, elem: int):
    low = 0
    high = len(arr) - 1

    answer = -1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > elem:
            low = mid + 1
        elif arr[mid] == elem:
            return mid
        else:
            high = mid - 1
            answer = mid

    return answer


# print(
#     climbingScoreboard(10, [95, 90, 80, 75, 70, 65, 60, 55, 50], 4,
#                        [55, 65, 100, 85]))

arr = [57, 55, 50, 46, 42, 35, 31, 27, 23, 20]
print(floor(arr, 36))
