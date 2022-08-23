def cf725A(n: int, numbers: list):
    max_left = max_index = numbers.index(n)
    max_right = n - max_left - 1
    min_left = min_index = numbers.index(1)
    min_right = n - min_left - 1

    curr = n
    
    # MAX Left
    temp = max_left
    if 0 <= min_index <= max_left:
        curr = min(curr, temp + 1)
    else:
        curr = min(curr, temp + min_right + 2, min_left + 1)
    
    # MAX Right
    temp = max_right
    if max_index <= min_index <= n:
        curr = min(curr, temp + 1)
    else:
        curr = min(curr, temp + min_left + 2, min_right + 1)

    return curr

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        numbers = list(map(int, input().split()))
        print(cf725A(n, numbers))
