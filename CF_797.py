for _ in range(int(input())):
    n = int(input()) - 6
    nums = [1, 3, 2]
    for i in range(n):
        nums[(i + 1) % 3] += 1

    print(*reversed(nums))
