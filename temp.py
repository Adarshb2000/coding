def recur(visited):
    if len(visited) == n:
        return 0
    if tuple(visited) in dp:
        return dp[tuple(visited)]
    ans = 10**5
    for i in range(n):
        if i not in visited:
            visited.add(i)
            for j in range(n):
                if j not in visited:
                    visited.add(j)
                    ans = min(ans, recur(visited.copy()) + (a[i] + a[j]) % k)
    dp[tuple(visited)] = ans
    return dp[tuple(visited)]


def method0(a, k):
    global dp
    sum_ = 0
    for i, val in enumerate(a):
        sum_ += val
        a[i] = a[i] % k
    dp = {}
    return (sum_ - recur(set())) // k


def brute(numbers, k):
    answer = 0
    nums = []
    for num in numbers:
        answer += num // k
        nums.append(num % k)

    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    if 0 in counts:
        counts[0] %= 2

    for i in range(1, k):
        if i not in counts:
            continue

        start = k - i
        while counts[i]:
            for j in range(start, k):
                if j in counts and counts[j]:
                    if i == j:
                        if counts[i] == 1:
                            continue
                    counts[j] -= 1
                    counts[i] -= 1
                    answer += 1
                    break
            else:
                break

    return answer

from random import randint
while True:
    global a, k
    n = 5
    numbers = [randint(1, 10) for _ in range(n)]
    a = numbers.copy()
    k = 3
    answer0 = method0(numbers.copy(), k)
    answer1 = brute(numbers.copy(), k)
    if answer0 != answer1:
        print(numbers, k)
        print(answer0)
        print(answer1)
        break
quit()

for _ in range(int(input())):
    _, k = map(int, input().split())
    print(CF797E(list(map(int, input().split())), k))