def spacearr(numbers):
    n = len(numbers)
    diff =  n * (n + 1) // 2 - sum(numbers)
    numbers = sorted(numbers)

    for i, number in enumerate(numbers, start=1):
        if i < number:
            return False

    return diff % 2


if __name__ == '__main__':

    t = int(input())

    while t:

        input()

        print('First' if spacearr(list(map(int, input().split()))) else 'Second')

        t -= 1