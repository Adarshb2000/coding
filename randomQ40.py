def max_div(n, k, a):
    MOD = 10 ** 9 + 7
    if k == 0:
        return 0 if 1 in a else pow(2, n - 1, MOD)

    if sum(a) <= k or sum(a) % k != 0:
        return 0
    
    nums = [0]
    temp = 0
    i = 0
    while i < n:
        if temp == k:
            if a[i]:
                temp = 0
                nums.append(0)
            else:
                nums[-1] += 1
        temp += a[i]
        i += 1
    
    if a[-1] == 0:
        nums.pop()
    
    answer = 1
    for num in nums:
        answer = (answer * (num + 1)) % MOD
    
    return answer

print(max_div(19, 4, [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]))

    