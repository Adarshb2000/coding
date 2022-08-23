def altaray(numbers):
    n = len(numbers)

    answer = [1] * n
    temp = [None] * (n - 1)

    for i in range(n - 1):
        temp[i] = numbers[i] * numbers[i + 1] < 0

    for i, change in enumerate(reversed(temp), start=2):
        if change:
            answer[-i] = answer[-i + 1] + 1
        
    return answer


if __name__ == '__main__':
    
    t = int(input())

    while t:
        input()

        print(*altaray(list(map(int, input().split()))))


        t -= 1

    # while x := list(map(int, input().split())):
    #     print(*altaray(x))
