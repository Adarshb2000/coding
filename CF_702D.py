def cf_702D(numbers: list, depth: int = 0):
    if not numbers: return
    num, index = max([num, i] for i, num in enumerate(numbers))
    answer[indices[num]] = depth
    cf_702D(numbers[: index], depth + 1)
    cf_702D(numbers[index + 1 :], depth + 1)

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        numbers = list(map(int, input().split()))
        answer = [None] * n
        indices = {num: i for i, num in enumerate(numbers)}
        cf_702D(numbers)
        print(*answer)