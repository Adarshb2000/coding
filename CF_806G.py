def recur(i, div, numbers, k):
    if i == len(numbers):
        return 0
    
    elif (i, div) in dp:
        return dp[(i, div)]
    
    dp[(i, div)] = max(recur(i + 1, div, numbers, k) + numbers[i] // div - k, recur(i + 1, div * 2, numbers, k) + numbers[i] // (div * 2))

    return dp[(i, div)]


def CF806G(numbers, k):
    return recur(0, 1, numbers, k)

if __name__ == '__main__':
    dp = {}
    for _ in range(int(input())):
        dp = {}
        _, k = map(int, input().split())
        print(CF806G(list(map(int, input().split())), k))