def quizplag(n, numbers):
    temp = set()
    dqfy = set()
    for num in numbers:
        if num <= n:
            if num in temp:
                dqfy.add(num)
            temp.add(num)
    
    answer = list(dqfy)
    answer.sort()
    return [len(answer)] + answer


if __name__ == '__main__':
    
    
    for _ in range(int(input())):
        n, _, _ = map(int, input().split())
        numbers = list(map(int, input().split()))
        print(*quizplag(n, numbers))